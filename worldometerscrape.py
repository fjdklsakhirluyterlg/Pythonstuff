import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

result = soup.find_all("div", "maincounter-number")
print(result[0].text)
print(result[1].text)
print(result[2].text)

def get_country_covid(country):
    URL = f"https://www.worldometers.info/coronavirus/country/{country}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find_all("div", "maincounter-number")
    print(result[0].text)
    print(result[1].text)
    print(result[2].text)

get_country_covid("uk")