# from parsel import Selector
# from playwright.sync_api import sync_playwright
# import re, json, time
# import csv
# import pandas as pd

# def scrape_institution_members(institution: str):
#     with sync_playwright() as p:
        
        
#         page_num = 1 
        
#         members_is_present = True
#         while members_is_present:
            
#             browser = p.chromium.launch(headless=True, slow_mo=50)
#             page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
#             page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}")
#             selector = Selector(text=page.content())
            
#             print(f"page number: {page_num}")
            
#             for member in selector.css(".nova-legacy-v-person-list-item"):
#                 name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
#                 link = f'https://www.researchgate.net/{member.css(".nova-legacy-v-person-list-item__align-content a::attr(href)").get()}'
#                 profile_photo = member.css(".nova-legacy-l-flex__item img::attr(src)").get()
#                 department = member.css(".nova-legacy-v-person-list-item__stack-item:nth-child(2) span::text").get()
#                 disciplines = member.css("span .nova-legacy-e-link::text").getall()
#                 print(name,"\n",link,"\n", department, "\n", disciplines, "\n\n")
                
#                 # institution_members.append({
#                 #     "name": name,
#                 #     "link": link,
#                 #     "profile_photo": profile_photo,
#                 #     "department": department,
#                 #     "disciplines": disciplines
#                 # })
#                 institution_members.append([name, link, profile_photo, department, disciplines])
#             # check for Page not found selector
#             if selector.css(".headline::text").get():
#                 members_is_present = False
#             else:
#                 time.sleep(2) # use proxies and captcha solver instead of this
#                 page_num += 1 # increment a one. Pagination
#             print (institution_members)

#         # print(json.dumps(institution_members, indent=2, ensure_ascii=False))
#         # print(len(institution_members)) # 624 from a EM-Normandie-Business-School

#         browser.close()
        

#         """
#         you can also render the page and extract data from the inline JSON string,
#         however, it's messy and from my perspective, it is easier to scrape the page directly.
#         """
        
#         # https://regex101.com/r/8qjfnH/1
#         # extracted_data = re.findall(r"\s+RGCommons\.react\.mountWidgetTree\(({\"data\":{\"menu\".*:true})\);;",
#         #                        str(page.content()))[0]
#         # json_data = json.loads(extracted_data)
#         # print(json_data)

# institution = "Poltekkes_Kemenkes_Malang"
# institution_members = []
# head_element = ["name", "link", "profile_photo", "department", "disciplines"]
# scrape_institution_members(institution)


# with open(f"institution_members_{institution}.csv", 'w') as csvfile:
# 	csvwriter = csv.writer(csvfile)
# 	csvwriter.writerow(head_element)
# 	csvwriter.writerows(institution_members)

# df = pd.read_csv(f"institution_members_{institution}.csv", encoding='unicode_escape')
# print(df.head(5)) 


from parsel import Selector
from playwright.sync_api import sync_playwright
import pandas as pd
import json, time, re

institution = "Central_South_University"
page_num = 1

# with sync_playwright() as p:
#     member_check = True
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}")
#     selection = Selector(text=page.content())

#     for member in selection.css(".nova-legacy-v-person-list-item"):
#         name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
#         print(name)
p = sync_playwright().start()
browser = p.chromium.launch(headless=True, slow_mo=50)
page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}")
selection = Selector(text=page.content())
member = selection.css(".nova-legacy-v-person-list-item")
name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
# link = member.css(".nova-legacy-v-person-list-item__align-content a::attr(href)").get()
link = member.css(".nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare a::attr(href)").get()
department = member.css(".nova-legacy-v-person-list-item__stack-item:nth-child(2) span::text").get()
disciplines = member.css("span .nova-legacy-e-link::text").getall()
print(name,"\n", link,"\n", department,"\n", disciplines)

selection.css(".headline::text").get()

browser.close()
p.stop()