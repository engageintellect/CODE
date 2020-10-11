import os
import subprocess
import time
import requests as req
from bs4 import BeautifulSoup as makesoup

os.system('clear')

# MAKE SOUP
page = req.get('https://suckless.org')
soup = makesoup(page.content, 'html.parser')
result = soup.prettify()
result_split = result.split()

# SEARCH THROUGH RESULTS FOR TEXT
a = result_split.index('software')
answer = str(result_split[int(a):int(a+4)])
answer = answer.replace(',','')
answer = answer.replace('[','')
answer = answer.replace(']','')
answer = answer.replace("'",'')

print(answer)


