from bs4 import BeautifulSoup
import requests


# GBP TO EUR
URL = "https://www.bbc.co.uk/news/topics/cx250jmk4e7t/pound-sterling-gbp"
response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
result = soup.find_all("div", class_="gel-paragon nw-c-md-currency-summary__value")
print(result)
print(result[0].text)

# FTSE 100

URL2 = "https://www.bbc.co.uk/news/topics/c9qdqqkgz27t/ftse-100"
response2 = requests.get(URL2)

soup2 = BeautifulSoup(response2.content, "html.parser")
result2 = soup2.find_all("div", class_="gel-paragon nw-c-md-market-summary__value")
print(result2[0].text)

# S&P 500
URL3 = "https://www.bbc.co.uk/news/topics/c4dldd02yp3t/sp-500"
response3 = requests.get(URL3)

soup3 = BeautifulSoup(response3.content, "html.parser")
result3 = soup3.find_all("div", class_="gel-paragon nw-c-md-market-summary__value")
print(result3[0].text)

# GOOGLE FINANCE SCRAPING
URL4 = "https://www.google.com/finance/quote/AAPL:NASDAQ"
response4 = requests.get(URL4)

soup4 = BeautifulSoup(response4.content, "html.parser")
result4 = soup4.find_all("div", class_="YMlKec fxKbKc")
print(result4[0].text)