from parsel import Selector
from playwright.sync_api import sync_playwright
import pandas as pd
import time
import csv

def scrape_institution_members(institution: str):
    with sync_playwright() as p:
        page_num = 1 
        members_is_present = True

        while members_is_present:
            
            browser = p.chromium.launch(headless=True, slow_mo=50)
            page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
            page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}", timeout = 0)
            selector = Selector(text=page.content())
            
            print(f"page number: {page_num}")
            
            for member in selector.css(".nova-legacy-v-person-list-item"):
                name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
                link = f'https://www.researchgate.net/{member.css(".nova-legacy-v-person-list-item__align-content a::attr(href)").get()}'
                profile_photo = member.css(".nova-legacy-l-flex__item img::attr(src)").get()
                department = member.css(".nova-legacy-v-person-list-item__stack-item:nth-child(2) span::text").get()
                disciplines = member.css("span .nova-legacy-e-link::text").getall()
                # print(name,"\n",link,"\n", department, "\n", disciplines, "\n\n")
                institution_members.append([name, link, profile_photo, department, disciplines])
            # check for Page not found selector
            if selector.css(".headline::text").get():
                members_is_present = False
            else:
                time.sleep(2) # use proxies and captcha solver instead of this
                page_num += 1 # increment a one. Pagination
            # print (institution_members)
            browser.close()

        # browser.close()
        

# institution = "Poltekkes_Kemenkes_Malang"
institution = "Central_South_University"


institution_members = []
head_element = ["name", "link", "profile_photo", "department", "disciplines"]
scrape_institution_members(institution)


with open(f"institution_members_{institution}.csv", 'w', encoding='UTF-8') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(head_element)
	csvwriter.writerows(institution_members)

df = pd.read_csv(f"institution_members_{institution}.csv", encoding='unicode_escape')
print(f"\ndata has {len(df)} rows x {len(df.columns)} columns\n")

print(df.head(5)) 
