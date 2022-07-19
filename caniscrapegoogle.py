import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=bugatti"
response  = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("h3", "LC20lb MBeuO DKV0Md")

print(result)