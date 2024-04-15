from parsel import Selector
from playwright.sync_api import sync_playwright
import json

article = "Three-dimensional audio magnetotelluric imaging of the Yangyi geothermal field in Tibet, China"
page_num = 1
publications = []

p = sync_playwright().start()
browser = p.chromium.launch(headless=True, slow_mo=50)
page = browser.new_page()
page.goto(f"https://www.researchgate.net/search/publication?q={article}&page={page_num}")
selector = Selector(text=page.content())

# publication = selection.css(".nova-legacy-c-card__body--spacing-inherit")
# title = publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::text").get().title()
# title_link = f'https://www.researchgate.net{publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::attr(href)").get()}'
# publication_type = publication.css(".nova-legacy-v-publication-item__badge::text").get()
# publication_date = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(1) span::text").get()
# publication_doi = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(2) span").xpath("normalize-space()").get()
# publication_isbn = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(3) span").xpath("normalize-space()").get()
# authors = publication.css(".nova-legacy-v-person-inline-item__fullname::text").getall()
# source_link = f'https://www.researchgate.net{publication.css(".nova-legacy-v-publication-item__preview-source .nova-legacy-e-link--theme-bare::attr(href)").get()}'

for publication in selector.css(".nova-legacy-c-card__body--spacing-inherit"):
    title = publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::text").get().title()
    title_link = f'https://www.researchgate.net{publication.css(".nova-legacy-v-publication-item__title .nova-legacy-e-link--theme-bare::attr(href)").get()}'
    publication_type = publication.css(".nova-legacy-v-publication-item__badge::text").get()
    publication_date = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(1) span::text").get()
    publication_doi = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(2) span").xpath("normalize-space()").get()
    publication_isbn = publication.css(".nova-legacy-v-publication-item__meta-data-item:nth-child(3) span").xpath("normalize-space()").get()
    authors = publication.css(".nova-legacy-v-person-inline-item__fullname::text").getall()
    source_link = f'https://www.researchgate.net{publication.css(".nova-legacy-v-publication-item__preview-source .nova-legacy-e-link--theme-bare::attr(href)").get()}'
    print(title,"\n",title_link,"\n",publication_type,"\n",publication_date,"\n",publication_doi,"\n",publication_isbn,"\n",authors,"\n",source_link,"\n","\n",)

    publications.append({
                    "title": title,
                    "link": title_link,
                    "source_link": source_link,
                    "publication_type": publication_type,
                    "publication_date": publication_date,
                    "publication_doi": publication_doi,
                    "publication_isbn": publication_isbn,
                    
                    "authors": authors
                })
    print(title,"\n",title_link,"\n",publication_type,"\n",publication_date,"\n",publication_doi,"\n",publication_isbn,"\n",authors,"\n",source_link,"\n","\n",)

browser.close()
p.stop()