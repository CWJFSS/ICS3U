from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip()
print (name)

name = name_box.text.strip() 
print (name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)

