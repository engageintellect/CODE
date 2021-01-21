#!/usr/bin/env python3

import os
import subprocess
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

    
    ###################
    # INIT WEB-DRIVER #
    ###################

#=[ headless driver ]=#
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')

#=[ regular driver ]=#
# driver = webdriver.Chrome()

driver.implicitly_wait(10)

    
    ###########
    # DISPLAY #
    ###########

def clear_display():
    os.system('clear')
    os.system('figlet github repo')
    print("\n")

clear_display()


    ###################
    # LOGIN TO GITHUB #
    ###################

##=[ github account info ]=#
# username = input("GITHUB USERNAME: ")
# password = input("GITHUB PASSWORD: ")

user = subprocess.getoutput("echo $USER")
local_path = os.environ['HOME']
username = 'jc9361'
password = 'evo9gsrSE'

clear_display()

driver.get("https://www.github.com/login")
driver.find_element_by_id("login_field").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_name("commit").click()


    ###################
    # CREATE NEW REPO #
    ###################

try:
    repo_name = sys.argv[1]
    print(f'REPO NAME: {repo_name}')
except:
    repo_name = input("REPO NAME: ")
finally:
    repo_description = input("REPO DESCRIPTION: ")
    repo_visability = input("PUBLIC OR PRIVATE REPO: ")
    if 'private' in repo_visability.lower():
        driver.get("https://www.github.com/new")
        driver.find_element_by_id("repository_visibility_private").click()
    else:
        driver.get("https://www.github.com/new")

driver.find_element_by_name("repository[name]").send_keys(repo_name)
driver.find_element_by_name("repository[description]").send_keys(repo_description)
# repo_address = str(driver.current_url)
repo_address = f'https://github.com/{username}/{repo_name}.git'

WebDriverWait(driver, 20).until(EC.element_to_be_clickable \
        ((By.CSS_SELECTOR, "button.btn.btn-primary.first-in-line"))).click()
    

    #############################
    # LINK LOCAL REPO TO REMOTE #
    #############################


#=[ local repo path ]=#

local_repo_path = input("ENTER FULL REPO PATH: ")

if local_repo_path == "":
    os.chdir(local_path)
    os.mkdir(repo_name)
    os.chdir(repo_name)
elif local_path == ".":
    pass
else:
    print(os.getcwd())
    os.chdir(f"{local_repo_path}")



#=[ initialize local repository ]=#
clear_display()
os.system('git init')
print(f'GitHub repository "{repo_name}" has been created.')

# remote add repository
os.system(f'git remote add origin {repo_address}')
print(f'REPO "{repo_name}" SUCCESSFULLY LINKED TO REMOTE BRANCH.')
print(f"Repository address: {repo_address}\n")
print(f'READY FOR FIRST COMMIT...\n')


    ######################
    # COMPLETION MESSAGE #
    ######################


#=[ add repo address to clipmenu ]=#
os.system(f'echo {repo_address} | xclip')

#=[ INITIAL COMMIT ]=#
git_acp = input("Would you like to do a first commit?(y/N): ")

if git_acp == 'y':
    commit_msg =  input("Enter a commit message: ")
    if commit_msg == '':
        commit_msg = 'Updating Repository...'
    else:
        pass

    # PUSH TO GITHUB
    os.system(f'git add . && git commit -m "{commit_msg}" && git push origin master')

else:
    clear_display()
    print("Exiting Program...")
    sleep(1)
    os.system('clear')
    quit()


driver.close()
os.system('clear')
quit()
