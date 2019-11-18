import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Sony-ILCE-6400L-Mirrorless-Digital-16-50mm/dp/B07NF6J8N5/ref=sr_1_1_sspa?keywords=sony+camera&qid=1568313509&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUE00NDdBTkYxSDFEJmVuY3J5cHRlZElkPUExMDA1ODUwUDg5Q042RjlCTThPJmVuY3J5cHRlZEFkSWQ9QTA3MzkxOTYzODZNTjBKVUdSVFQxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    title=soup.find(id="title").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()#string
    converted_price=price[1:8]
    converted_price1=float(price[1:4]+price[5:8])
    print(converted_price1)

    if(converted_price1 > 74000.0):
            send_mail()
    print(title.strip())
    print(price.strip())

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('122015021@sastra.ac.in','thunder0101')
    subject='price fell down'
    body='https://www.amazon.in/Sony-ILCE-6400L-Mirrorless-Digital-16-50mm/dp/B07NF6J8N5/ref=sr_1_1_sspa?keywords=sony+camera&qid=1568313509&s=gateway&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUE00NDdBTkYxSDFEJmVuY3J5cHRlZElkPUExMDA1ODUwUDg5Q042RjlCTThPJmVuY3J5cHRlZEFkSWQ9QTA3MzkxOTYzODZNTjBKVUdSVFQxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(

        '122015021@sastra.ac.in','rohitchatla@gmail.com',msg
    )
    print('HEY email.has been sent')
    server.quit()

while(True):
    check_price()
    time.sleep(60)