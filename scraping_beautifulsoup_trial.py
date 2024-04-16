# import requests
# from bs4 import BeautifulSoup

# # download the target page
# url= "https://www.researchgate.net/institution/Central_South_University/members"
# response = requests.request('GET', url)
# content = response.content.decode('utf-8')
# # parse the HTML content of the page
# # soup = BeautifulSoup(content, 'html.parser')
# soup = BeautifulSoup(response.text, 'lxml')

# profile = soup.find("div",class_="nova-legacy-o-stack__item institution-members-list")
# # author = profile.find("div", class_="nova-legacy-v-person-list-item__align-content")
# # author_name = profile.find("h5").get_text()
# # print(author_name)
# print(profile)


# from bs4 import BeautifulSoup
# from urllib.request import urlopen, Request

# institution = "Poltekkes_Kemenkes_Malang"
# page_num = 1

# url = f"https://www.researchgate.net/institution/{institution}/members/{page_num}"
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# site = urlopen(req).read()

# soup = BeautifulSoup(site, "html.parser")
# member_list = soup.find("div", class_ = "nova-legacy-o-stack__item institution-members-list")
# print(member_list)


# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup

# # # site = "https://www.cmegroup.com/markets/products.html?redirect=/trading/products/"
# site = "https://www.cmegroup.com/"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# req = Request(
#     url=site, 
#     headers=headers
# )
# webpage = urlopen(req).read()
# print(webpage.content)
# soup = soup = BeautifulSoup(webpage, "html.parser")
# member_list = soup.find("div", class_ = "main-table-wrapper")
# print(member_list)

import requests
url = "https://www.cmegroup.com/"
# url = 'http://www.ichangtou.com/#company:data_000008.html'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
headers = {

'Accept':'application/json',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'en-US,en;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Content-Length':'1906',
'Content-Type':'application/json;charset=UTF-8',
'Cookie':'JSESSIONID=47557C2D51CF5D41467BEB15ABBACAC8; glide_user_route=glide.79dba59629920b67318b94e9ba748ce8; BIGipServerpool_fccprod=2407616266.46142.0000; __CJ_g_startTime=%221642015559308%22',
'Host':'fccprod.servicenowservices.com',
'Origin':'https',
'Pragma':'no-cache',
'Referer':'https',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
# 'x-portal':'ac2856301b92681048c6ed7bbc4bcb27',
# 'X-Transaction-Source':'Interface=Service-Portal,Interface-Type=rmd,Interface-SysID=ac2856301b92681048c6ed7bbc4bcb27',
# 'X-UserToken':'a78bb85d1b418910222b0e9ee54bcb7b42f1e8f0a87eeb85195b6c731e5ad46b032c7e8a',
}
response = requests.get(url, headers=headers)
print(response.content)