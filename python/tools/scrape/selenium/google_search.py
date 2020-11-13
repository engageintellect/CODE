from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com")


# driver.find_element_by_class_name("gLFyf").click()
driver.find_element_by_class_name("gLFyf").send_keys("hello world")

driver.find_element_by_class_name("gNO89b").click()
