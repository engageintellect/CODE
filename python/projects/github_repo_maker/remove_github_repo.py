import os
import sys
from time import sleep

import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

    ###########
    # DISPLAY #
    ###########

def display():
    os.system('clear')
    os.system('figlet delete repo')
    print('\n')

def clear():
    os.system('clear')

display()


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


    ##################
    #  GITHUB MAGIC  #
    ##################


username = 'jc9361'
password = 'evo9gsrSE'

driver.get("https://www.github.com/login")
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()

repos = f"https://www.github.com/{username}?tab=repositories"
driver.get(repos)


    #########################
    #  GET/PRINT REPO LIST  #
    #########################

repo_list = []
page = req.get(repos)
soup = bs(page.content, "html.parser")

for i in soup.find_all('a'):
    if f'/{username}/' in i.get('href'):
        repo_list.append(i.get('href'))

print('#===[ REPO LIST ]===#\n')
for x in repo_list:
    print(x)
print('\n')



    ###########################
    #  CHOOSE REPO TO DELETE  #
    ###########################

repo_name = input("ENTER REPO NAME TO DELETE: ")
if username in repo_name:
    repo_name = repo_name.replace(username, '').replace('/', '')
else:
    pass

# GO TO REPO SETTINGS PAGE AND SCROLL TO BOTTOM
repos = f"https://www.github.com/{username}/{repo_name}/settings"
driver.get(repos)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# TRY REPO DELETE (FOR PUBLIC REPOS)
try:
    delete_button = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary').click()
    delete_prompt = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input') \
            .send_keys(f'{username}/{repo_name}')
    delete_prompt_button = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button')

# EXCEPT REPO DELETE (FOR PRIVATE REPOS)
except:
    delete_button = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary').click()
    delete_prompt = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input') \
            .send_keys(f'{username}/{repo_name}')
    delete_prompt_button = driver.find_element_by_xpath \
            ('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')



# CONFIRM REPO DELETE
display()
are_you_sure = input(f'ARE YOU SURE YOU WANT TO DELETE {repo_name}?(y/N): ')
if 'y' or 'Y' in are_you_sure:
    delete_prompt_button.click()
else:
    display()
    print('Well... That was close...')
    sleep(2)
    driver.close()
    clear()
    quit()



# EXIT ROUTINE
driver.close()
print(f'REPO {repo_name} has been removed.')
sleep(3)
clear()
quit()
