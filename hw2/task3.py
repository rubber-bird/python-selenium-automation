from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

# open the url
driver.get('https://www.amazon.com')
sleep(3)

order_button = driver.find_element(By.XPATH , "//div[@class='nav-right']//div[@class='layoutToolbarPadding']//a[@id='nav-orders']//span[@class='nav-line-2']")

order_button.click()

assert 'Sign-In' in driver.find_element(By.XPATH, "//h1").text

sleep(2)
driver.quit()