from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://suckless.org')



element = driver.find_element_by_partial_link_text("tools")

element.click()



