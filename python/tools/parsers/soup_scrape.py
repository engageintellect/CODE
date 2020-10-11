import requests as req
from bs4 import BeautifulSoup as bs
import os
import subprocess
import time


url = 'https://newyorktimes.com'

page = req.get(url)
soup = bs(page.content, "html.parser")


print(soup.prettify())

# STRIP TAGS

# print(soup.text.split())


# PRINT CLEANED LIST

# for x in soup.text.split():
#     print(x)



