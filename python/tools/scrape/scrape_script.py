import subprocess
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as req

url = 'https://www.bestbuy.com/site/all-laptops/pc-laptops/pcmcat247400050000.c?id=pcmcat247400050000'

page =  req(url)
page_html = page.read()
page.close()

page_soup = bs(page_html, "html.parser")

results = page_soup.findAll("div", {"class":"list-item lv"})



print(results)





