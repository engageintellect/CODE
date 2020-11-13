from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# OPTIONS FOR SELENIUM...
options = Options()
options.add_argument("--incongnito")
driver = webdriver.Chrome(options=options, 
        executable_path="/usr/bin/chromedriver")


# URL
url = input("enter a url: ")
driver.get(url)

# BROWSER DETAILS
print(driver.title)
print(driver.current_url)
# print(driver.window_handles)
# print(driver.page_source)

# NAVIGATION
sleep(2)
driver.get('https://suckless.org')
sleep(2)
driver.back()
sleep(2)
driver.forward()
driver.refresh()

