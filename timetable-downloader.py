import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime

my_url = 'http://www.fiitjeeeastdelhi.com/time_table.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html , "html.parser")
containers = page_soup.find("a" , {"href" : "TT.pdf"})
contain = containers["href"]
my_url = my_url[:-16]
final_url = my_url + '/' + contain
now = datetime.datetime.now()
date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) 
# filename = date + '.pdf'
urllib.request.urlretrieve(final_url , "time_table")