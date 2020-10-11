import requests
from bs4 import BeautifulSoup as bs

# get the page
#url = 'https://www.worldometers.info/coronavirus/'
url = 'https://www.reddit.com/r/unixporn/'

page = requests.get(url)
# make soup
soup = bs(page.text, 'html.parser')

# get data simply by looking for each tr
for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        # remove (.text) to show td tags
        print(td.text)


for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        # remove (.text) to show td tags
        print(td.text)

