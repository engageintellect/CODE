
import requests
from bs4 import BeautifulSoup as bs

#page = requests.get("https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=los+angeles%2C+CA")
page = requests.get("https://www.worldometers.info/coronavirus/")

soup = bs(page.content)

# print all lines
#for link in soup.find_all('a'):
#    print(link)

# print all links "href"
#for link in soup.find_all('a'):
#    print(link.get('href'))

# print all lines as text
for link in soup.find_all('a'):
    print(link)

# print soup (pretty)
#print(soup.prettify())
