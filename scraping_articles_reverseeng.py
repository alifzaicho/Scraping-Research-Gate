from parsel import Selector
from playwright.sync_api import sync_playwright
import json

def scrape_researchgate_publications(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36")
        
        publications = []
        page_num = 2
        
        page.goto(f"https://www.researchgate.net/search/publication?q={query}&page={page_num}")
        selector = Selector(text=page.content())
        for publication in selector.css(".nova-legacy-c-card__body--spacing-inherit"):
            title = publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::text").get().title()
            print(title)


query = "Three-dimensional audio magnetotelluric imaging of the Yangyi geothermal field in Tibet, China"
scrape_researchgate_publications(query)