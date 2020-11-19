from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--headless")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options,
        executable_path="/usr/bin/chromedriver")

driver.get('https://reddit.com/r/wallpapers')

images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))

driver.close()
