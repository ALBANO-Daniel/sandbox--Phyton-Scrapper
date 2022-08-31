import requests
from bs4 import BeautifulSoup
import smtplib

re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
res = re.content

soup = BeautifulSoup(res, 'html.parser')

price = soup.find('p', class_='price_color').text[1:]

price = float(price)

if price < 60:
    smt = smtplib.SMTP('smtp.fakemail.net', )
    smt.ehlo()
    smt.starttls()
    smt.login('lowen.dezi@aladeen.org', 'xumbj6G&')
    smt.sendmail('lowen.dezi@aladeen.org', 'glockglock@gmail.com', f"Subject: Price\n\n Hi, price is {price}.")
    smt.quit()



# print(soup.prettify())

# print(res)