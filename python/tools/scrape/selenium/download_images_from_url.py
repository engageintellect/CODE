from selenium import webdriver

import os, subprocess, sys

# OPTIONS
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--test-type")
options.add_argument("--headless")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options, 
        executable_path="/usr/bin/chromedriver")

url = input("Enter a URL to scrape for images: ")

driver.get(url)

images = driver.find_elements_by_tag_name('img')
image_list = []

for image in images:
    print(image.get_attribute('src'))
    image_list.append(image.get_attribute('src'))
driver.close()

download_or_no = input("\nDownload images? (y/n): ")

if download_or_no == 'y':
    page_name = input("Name folder to download images to: ")
    os.mkdir(page_name)
    os.chdir(page_name)
    for x in image_list:
        os.system('wget ' + x)
else:
    quit()

