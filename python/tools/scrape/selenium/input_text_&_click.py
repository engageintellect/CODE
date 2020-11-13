from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://google.com')


search = driver.find_element_by_class_name("gLFyf").click()


driver.find_element_by_class_name("gLFyf").send_keys("hello worlddd")









