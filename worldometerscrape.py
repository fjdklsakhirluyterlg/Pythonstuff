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
    x = []
    URL = f"https://www.worldometers.info/coronavirus/country/{country}"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find_all("div", "maincounter-number")
    x.append(result[0].text)
    x.append(result[1].text)
    x.append(result[2].text)
    return x

get_country_covid("uk")