# # Import libraries to deploy into scraper 
# import asyncio 
# from playwright.async_api import Playwright, async_playwright 
# import csv

# # Start with playwright scraping here: 
# async def scrape_data(page): 
# 	scraped_elements = [] 
# 	items = await page.query_selector_all("li.product") 
 
# 	# Pick the scraping item 
# 	for i in items: 
# 		scraped_element = {} 
 
# 		# Product name 
# 		el_title = await i.query_selector("h2") 
# 		scraped_element["product"] = await el_title.inner_text() 
 
# 		# Product price 
# 		el_price = await i.query_selector("span.woocommerce-Price-amount") 
# 		scraped_element["price"] = await el_price.text_content() 
 
# 		scraped_elements.append(scraped_element) 
# 	return scraped_elements 
 
 
# async def run(playwright: Playwright) -> None: 
# 	# Launch the headed browser instance (headless=False) 
# 	# To see the process of playwright scraping 
# 	# chromium.launch - opens a Chromium browser 
# 	browser = await playwright.chromium.launch(headless=False) 
 
# 	# Creates a new browser context 
# 	context = await browser.new_context() 
 
# 	# Open new page 
# 	page = await context.new_page() 
 
# 	# Go to the chosen website 
# 	await page.goto("https://scrapeme.live/shop/") 
# 	data = await scrape_data(page) 
 
# 	print(data) 
 
# 	await context.close() 
# 	# Turn off the browser once you finished 
# 	await browser.close() 

# def save_as_csv(data): 
# 	with open("scraped_data.csv", "w", newline="") as csvfile: 
# 		fields = ["product", "price", "img_link"] 
# 		writer = csv.DictWriter(csvfile, fieldnames=fields, quoting=csv.QUOTE_ALL) 
# 		writer.writeheader() 
# 		writer.writerows(data.values())

# async def main() -> None: 
# 	async with async_playwright() as playwright: 
# 		await run(playwright) 
 
 
# asyncio.run(main())
# # save_as_csv("data_scraping_trial.csv")


from playwright.sync_api import sync_playwright
import csv
import json
import pandas as pd

element_list = []
head_element = ["author", "quote"]
def main():
	with sync_playwright() as p:
		browser = p.chromium.launch(headless=False)
		page = browser.new_page()
		page.goto('https://quotes.toscrape.com/')
		all_quotes = page.query_selector_all('.quote')


		for quote in all_quotes:
			text = quote.query_selector('.text').inner_text()
			author = quote.query_selector('.author').inner_text()
			# print({'Author': author, 'Quote': text})
			element_list.append([author, text])
			# for i in range(len(author)):
			# 	element_list.append([author[i], text[i]])
			# 	print(len(author))
			# 	print(author)

		page.wait_for_timeout(3000)
		browser.close()


if __name__ == '__main__':
	main()

# file = open('quotes.json', mode='w', encoding='utf-8')
# file.write(json.dumps(element_list))	
# writer = csv.writer(open("quotes.csv", 'w'))
# for quotes in element_list:
#     writer.writerow(quotes)

with open("quotes.csv", 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(head_element)
	csvwriter.writerows(element_list)

df = pd.read_csv('quotes.csv', encoding='unicode_escape')
print(df) 