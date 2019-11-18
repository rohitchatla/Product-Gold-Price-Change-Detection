
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re
URL='https://www.bankbazaar.com/gold-rate-chennai.html'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    # title=soup.find(id="title").get_text()
    price=soup.findAll("td", {"class":"upvalue"})[0].get_text()
    # priced=price[3:]

    priced=int(re.search(r'\d+', price).group())
    print(priced)
    print('ok')

    # if(price > 74000.0):
    #then only it will work or else it
    priceplus=soup.find("table",{"class":"upvalue"})[2].get_text()



    send_mail(priced)



def send_mail(price):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('122015021@sastra.ac.in','thunder0101')
    subject='Gold price in Chennai'
    body=f"upvalue:{price}"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(

        '122015021@sastra.ac.in','rohitchatla@gmail.com',msg
    )
    print('HEY email.has been sent')
    server.quit()

while(True):
    check_price()

    time.sleep(60)