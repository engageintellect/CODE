from bs4 import BeautifulSoup as bs
import requests as req
import subprocess
subprocess.call('clear', shell=True)



url = input("Enter a site to scrape: ")



page = req.get(url)
soup = bs(page.content, 'html.parser')
for i in soup.find_all('a'): # It helps to find all anchor tag's
    print(i.get('href'))
