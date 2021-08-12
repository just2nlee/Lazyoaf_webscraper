

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.lazyoaf.com/collections/mens-t-shirts"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

tee_items  = html_soup.find_all('div', class_="product-bottom text-center")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for tee in tee_items:
    
    title = tee.find('a', class_="lower").text
    price = tee.find('span', class_="money").text
    

    f.write(title + ',' + price)

f.close()