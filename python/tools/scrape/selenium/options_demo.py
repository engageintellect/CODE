from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--icognito")



driver = webdriver.Chrome(options=options, 
        executable_path='/usr/bin/chromedriver')

driver.get('https://suckless.org')
