from parsel import Selector
from playwright.sync_api import sync_playwright
import re, json, time
import requests
from bs4 import BeautifulSoup

def scrape_institution_members(institution: str):
    with sync_playwright() as p:
        
        institution_memebers = []
        page_num = 1 
        
        members_is_present = True
        while members_is_present:
            
            browser = p.chromium.launch(headless=True, slow_mo=50)
            page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
            page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}")
            selector = Selector(text=page.content())
            
            print(f"page number: {page_num}")
            # response = requests.request('GET', url)
            # content = response.content.decode('utf-8')
            # parse the HTML content of the page
            # soup = BeautifulSoup(content, 'html.parser')
            soup = BeautifulSoup(response.text, 'lxml')
            profile = soup.find("div",class_="nova-legacy-o-stack__item institution-members-list")
            for member in selector.css(".nova-legacy-v-person-list-item"):
                # name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
                name = member.css(
                    ".nova-legacy-v-person-list-item__align-content .nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare::text").text_content()
                print(name)
                link = f'https://www.researchgate.net{member.css(".nova-legacy-v-person-list-item__align-content a::attr(href)").get()}'
                profile_photo = member.css(".nova-legacy-l-flex__item img::attr(src)").get()
                department = member.css(".nova-legacy-v-person-list-item__stack-item:nth-child(2) span::text").get()
                desciplines = member.css("span .nova-legacy-e-link::text").getall()
                
                institution_memebers.append({
                    "name": name,
                    "link": link,
                    "profile_photo": profile_photo,
                    "department": department,
                    "descipline": desciplines
                })
                
            # check for Page not found selector
            if selector.css(".headline::text").get():
                members_is_present = False
            else:
                time.sleep(2) # use proxies and captcha solver instead of this
                page_num += 1 # increment a one. Pagination

        print(json.dumps(institution_memebers, indent=2, ensure_ascii=False))
        print(len(institution_memebers)) # 624 from a EM-Normandie-Business-School

        browser.close()
        
        """
        you can also render the page and extract data from the inline JSON string,
        however, it's messy and from my perspective, it is easier to scrape the page directly.
        """
        
        # https://regex101.com/r/8qjfnH/1
        # extracted_data = re.findall(r"\s+RGCommons\.react\.mountWidgetTree\(({\"data\":{\"menu\".*:true})\);;",
        #                        str(page.content()))[0]
        # json_data = json.loads(extracted_data)
        # print(json_data)
    
scrape_institution_members(institution="Poltekkes_Kemenkes_Malang")