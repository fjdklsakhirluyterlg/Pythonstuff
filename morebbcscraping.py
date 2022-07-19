import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.co.uk/news"

response  = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("span", "gs-c-promo-heading__title gel-pica-bold")

x = []

for i in result:
    x.append(i.text)

print(x[-10:])