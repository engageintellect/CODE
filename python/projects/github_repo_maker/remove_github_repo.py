import os
import sys
from time import sleep

import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

    
    ###################
    # INIT WEB-DRIVER #
    ###################

##=[ headless driver ]=#
#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.add_argument('--headless')
#driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')

#=[ regular driver ]=#
driver = webdriver.Chrome()
driver.implicitly_wait(10)

username = 'jc9361'
password = 'evo9gsrSE'

driver.get("https://www.github.com/login")
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()

repos = f"https://www.github.com/{username}?tab=repositories"
driver.get(repos)

page = req.get(repos)
soup = bs(page.content, "html.parser")
for i in soup.find_all('a'):
    print(i.get('href'))

repo_name = input("enter repo name: ")






repos = f"https://www.github.com/{username}/{repo_name}/settings"
driver.get(repos)




repo_address = f" echo jc9361/{repo_name} | xclip"
os.system(f"{repo_address}")
quit()







