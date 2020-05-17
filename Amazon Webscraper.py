import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.com/Bush-Furniture-Shaped-Computer-Espresso/dp/B005EOL812/ref=sr_1_1_sspa?crid=31274GDNB43WK&dchild=1&keywords=computer+desk&qid=1589494770&sprefix=computer%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyU1dGUTVVSTFFRFY2JmVuY3J5cHRlZElkPUEwNDQxNzM5M1NMRVNDRVZXOFNSNSZlbmNyeXB0ZWRBZElkPUEwNTQyMzQ5WVNUWU9EQkJVUTc1JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
def check_price():
	page = requests.get(URL,headers=headers)
	soup1 = BeautifulSoup(page.content, 'html.parser')
	soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
	title = soup2.find(id= "productTitle").get_text()
	price = soup2.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[1:7])
	if(converted_price < 300):
		send_mail()
	print(title.strip())
	print(converted_price)
def send_mail():
	server=smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('dlcdrummer@gmail.com','Poopedon7777777!')
	subject='PRICE FELL DOWN!'
	body='Here is the Amazon link: https://www.amazon.com/Bush-Furniture-Shaped-Computer-Espresso/dp/B005EOL812/ref=sr_1_1_sspa?crid=31274GDNB43WK&dchild=1&keywords=computer+desk&qid=1589494770&sprefix=computer%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyU1dGUTVVSTFFRFY2JmVuY3J5cHRlZElkPUEwNDQxNzM5M1NMRVNDRVZXOFNSNSZlbmNyeXB0ZWRBZElkPUEwNTQyMzQ5WVNUWU9EQkJVUTc1JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
	msg = f"Subject: {subject}\n\n{body}"
	server.sendmail('dlcdrummer@gmail.com','dlcdrummer@gmail.com', msg)
	print('Email has been sent')
	server.quit()
check_price()


