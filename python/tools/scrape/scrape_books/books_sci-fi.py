import subprocess
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as req

# url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=x220&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=x20'
url = 'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html'

page =  req(url)
page_html = page.read()
page.close()

page_soup = bs(page_html, "html.parser")


results = page_soup.findAll("ol", {"class":"row"})


for x in results:
    x = x.text.strip()
    print(x)
















# result = page_soup.findAll("h3", {"class":"s-item_title"})
# results = page_soup.findAll("div", {"class":"s-item_title"})
# print(result)





