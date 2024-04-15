import requests
from bs4 import BeautifulSoup

# download the target page
url= "https://www.researchgate.net/institution/Central_South_University/members"
response = requests.request('GET', url)
content = response.content.decode('utf-8')
# parse the HTML content of the page
# soup = BeautifulSoup(content, 'html.parser')
soup = BeautifulSoup(response.text, 'lxml')

profile = soup.find("div",class_="nova-legacy-o-stack__item institution-members-list")
# author = profile.find("div", class_="nova-legacy-v-person-list-item__align-content")
# author_name = profile.find("h5").get_text()
# print(author_name)
print(profile)