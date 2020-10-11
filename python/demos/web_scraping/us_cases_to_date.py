import requests
from bs4 import BeautifulSoup as bs

# url to page
url = "https://www.worldometers.info/coronavirus/country/us/"

# page request
page = requests.get(url)
# soup parser
soup = bs(page.content, "html.parser")
# search for element
results = soup.find(id='maincounter-wrap')
# refine results...
content = str(results.find('span'))
content = content.split()
r = content[1].split('>')

# total
total = r[1]

# print total
print('TOTAL US CASES: ' + total)


