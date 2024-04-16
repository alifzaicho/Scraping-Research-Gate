from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

# url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
# res = requests.get(url)
# # soup = BeautifulSoup(res.text)
# # soup = BeautifulSoup(res.text, 'lxml')
# soup = BeautifulSoup(res.content, features="lxml")

# movies = soup.select("div.sc-ab6fa25a-3 bVYfLY dli-parent a")
# cok = movies.select(class_ = "ipc-title__text")
# print(cok)
table = []
wiki_link = "https://en.wikipedia.org/wiki/Wikipedia"
html = urlopen(wiki_link).read()
soup = BeautifulSoup(html, 'html.parser')

categories_table = soup.find("div", {"id": "mw-normal-catlinks"})
for each in categories_table.find_all("li"):
    link = each.find("a", href=True)
    print(each.text)
    print(link['href'], "\n")
    # print(categories_table.find("a" "li", href=True)["href"])
    
