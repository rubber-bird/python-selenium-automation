from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com')

help_button = driver.find_element(By.XPATH, "//li[@class='nav_last']/a[@class='nav_a'][text()='Help']").click()

sleep(3)

search_field = driver.find_element(By.XPATH ,"//div[@class='a-column a-span10']//div['a-row']//input[@class='a-input-text a-span12']")
go_button = driver.find_element(By.XPATH ,"//div[@class='a-column a-span2 a-span-last']//span[@class='a-button a-button-span12 a-button-base a-button-dark']//input[@class='a-button-input']")


search_field.send_keys('cancel order')
go_button.click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large a-color-offset-background answer-box']//div[@class='help-content']//h1[text()='Cancel Items or Orders']").text

sleep(2)
driver.quit()