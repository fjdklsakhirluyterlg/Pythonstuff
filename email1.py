import smtplib
import ssl
from email.message import EmailMessage
import requests
import datetime
from newsapi import NewsApiClient

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
         
        # printing all trending news
        print(i + 1, results[i])
    
    return results

def get_bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()

    return data["bpi"]["USD"]["rate"]

def send_email():
    sender_email = "drive.banerjee.armaan@gmail.com"
    receiver_email = "banerjee.armaan@gmail.com"
    password = "Transport11."
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
            
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
subject = "Roundup"
body = f"The bitoin price is {x} and the date tiem is {y}. \n The current top headlines are {l}"
send_email()