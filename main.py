import requests
from bs4 import BeautifulSoup
import smtplib

USERNAME = "yourmail2@gmail.com"
PASSWORD = "PASSWORD"
PRICE = 200.00

URL = "https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Expandable-Infinite/dp/B0BLW47H3M/ref=sr_1_1_sspa?crid=3CIPDHREMKDFY&keywords=samsung%2Ba14&qid=1693114144&sprefix=samsung%2Ba1%2Caps%2C583&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers = {
    "User-Agent": "YOUR HTTP HEADER FOR USER-AGENT",
    "Accept-Language": "YOUR HTTP HEADER FOR ACCEPT-LANGUAGE"
}

amazon_phone_req = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(amazon_phone_req.text, "lxml")

title = soup.find(name="span", class_="a-size-large product-title-word-break").get_text()
price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])

if price < PRICE:
    # Send email when price is lower
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs="yourmail@gmail.com",
                            msg=f"Subject: Amazon Price Alert!\n\n{title} is now ${price}\n\n{URL}")
