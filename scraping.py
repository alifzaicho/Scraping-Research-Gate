# importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import *
import csv
import json

# for holding the resultant list
element_list = []
 
for page in range(1, 3, 1):
 
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver = webdriver.Chrome()
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")
 
    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])
        print(len(title))
        print(title)
 
print(element_list)
 
#closing the driver
driver.close()
        
file = open('movies.json', mode='w', encoding='utf-8')
file.write(json.dumps(element_list))
 
writer = csv.writer(open("movies.csv", 'w'))
for movie in element_list:
    writer.writerow(movie.values())