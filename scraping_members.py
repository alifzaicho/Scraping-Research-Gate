from parsel import Selector
from playwright.sync_api import sync_playwright
import pandas as pd
import json, time, re

institution = "Central_South_University"
page_num = 2

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
page = browser.new_page()
page.goto(f"https://www.researchgate.net/institution/{institution}/members/{page_num}")
selection = Selector(text=page.content())
member = selection.css(".nova-legacy-v-person-list-item")
name = member.css(".nova-legacy-v-person-list-item__align-content a::text").get()
print(name)
browser.close()
p.stop()