import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.co.uk/news"
response2  = requests.get(URL)

soup2 = BeautifulSoup(response2.content, "html.parser")
result2 = soup2.find_all("a", {'class': "gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs"})

for i in result2:
    x = i.get("href")
    print(x)

