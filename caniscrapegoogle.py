import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.co.uk/news"
response  = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("a", {'class': "gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs"})

for i in result:
    x = i.get("href")
    print(x)

