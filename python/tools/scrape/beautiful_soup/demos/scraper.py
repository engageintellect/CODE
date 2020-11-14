import requests
from bs4 import BeautifulSoup as bs

#page = requests.get('https://www.worldometers.info/coronavirus/#countries')
page = requests.get('https://www.reddit.com/r/unixporn/')
soup = bs(page.content, 'html.parser')

results = soup.find(id='main_table_countries_today')

# SHOW CONTENT AS TEXT
#content = results.get_text()

# PRINT CONTENT
#print(content)
#print(content[-107:])

# PRINT PRETTY
print(soup.prettify())
