import requests
from bs4 import BeautifulSoup
import smtplib
import time
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("KEY")
EMAIL = os.getenv("EMAIL")

URL = 'https://www.amazon.com/iRobot-Roomba-675-Connectivity-Carpets/dp/B07DL4QY5V/ref=sr_1_3?dchild=1&keywords=roomba&qid=1587854652&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}


def check_price(): 
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    price = soup2.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[1:5])

    if(converted_price < 150):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL, KEY)

    subject = 'Price dropped!'
    body = 'https://www.amazon.com/iRobot-Roomba-675-Connectivity-Carpets/dp/B07DL4QY5V/ref=sr_1_3?dchild=1&keywords=roomba&qid=1587854652&sr=8-3'


    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        EMAIL,
        EMAIL,
        message
    )

    print('SENT EMAIL')

    server.quit()


check_price()
