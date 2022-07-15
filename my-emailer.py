import smtplib
import ssl
from email.message import EmailMessage
import requests
import datetime
from newsapi.newsapi_client import NewsApiClient
import os
import psutil

def get_battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    precent = battery.percent
    return f"The battery percent is {precent} and is plugged is {plugged}"

def USD_currency_converter():
    key = "1847R4PWRKL6J1IR"

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=USD&apikey={key}'
    r = requests.get(url)
    data = r.json()
    l = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return l

def EUR_currency_converter():
    key2 = "1847R4PWRKL6J1IR"

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GBP&to_currency=EUR&apikey={key2}'
    ryu = requests.get(url)
    data5 = ryu.json()
    u = data5["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return u

def is_tube_on():
    list = ["District", "Central", "Circle", "Piccadilly", "Bakerloo", "Hammersmith-City", "Jubilee", "Metropolitan", "Victoria", "Northern"]
    bad = []
    status_bad = []
    r = []

    for line in list:
        reply = requests.get("https://api.tfl.gov.uk/Line/" + line + "/Status")

        data = reply.json()

        Status = (data[0]["lineStatuses"][0]["statusSeverityDescription"])

        if Status != "Good Service":
            bad.append(line)
            status_bad.append(Status)
    
    for l in bad:
        response = requests.get(f"https://api.tfl.gov.uk/Line/{l}/Status")

        d = response.json()

        reason = (d[0]["lineStatuses"][0]["reason"])
        r.append(reason)
    
    return r
    
    

def file_size():
    return os.path.getsize("/Users/mohuasen/")

def get_news():
    API_KEY = "fb8efc5dab7249cca1ee3daa7e6ca278"
    newsapi = NewsApiClient(api_key='API_KEY')
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "fb8efc5dab7249cca1ee3daa7e6ca278"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
        print(i + 1, results[i])
    
    return results

def get_bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    return data["bpi"]["GBP"]["rate"]

def send_email():
    sender_email = "drive.banerjee.armaan@gmail.com"
    receiver_email = "banerjee.armaan@gmail.com"
    password = "ixsrblyncyrupttv"
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <br>
            <p style="text-align:center">{body}</p>
            <br>
            <h2> News </h2>
            <p>{body2}</p>
            <br>
            <h2> TFL</h2>
            <p>{body3}</p>
            <br>
            <h2> Currency conversion </h2>
            <p>{body4}</p>
            <p>{body5}</p>
            <br>
            <H2> Battery</H2>
            <p>{body6}</p>
            <br>
            <h2> Links</h2>
            <a href="https://www.bbc.co.uk">BBC</a>
            <a href="https://sites.google.com/view/revisionthingymajogy">Revision</a>


        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    print("Sending Email!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Success")

x = get_bitcoin()
y = datetime.datetime.now()
l = get_news()
g = file_size()
n = is_tube_on()
ii = USD_currency_converter()
jj = EUR_currency_converter()
zz = get_battery()
subject = "Roundup"
body = f"The bitoin price is {x} and the date tiem is {y}. \n The curretn file size is {g}"
body2 = f"The current top headlines are {l}"
body3 = n
body4 = f"The GPB is worth {ii} dollars"
body5 = f"The GPB is worth {jj} euros"
body6 = zz
send_email()
