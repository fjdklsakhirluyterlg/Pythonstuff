import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.co.uk/news/uk-politics-62228522"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("p", "ssrcss-ugte5s-Contributor strong")
print(result)