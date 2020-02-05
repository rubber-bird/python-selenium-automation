from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

driver.get('https://www.amazon.com/')
sleep(2)

orders_button = driver.find_element(By.XPATH, "//div[@class='nav-right']//div[@class='layoutToolbarPadding']//a[@class='nav-a nav-a-2  ']//span[text()='& Orders']")
orders_button.click()

sleep(2)

assert 'Sign-In' in driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-base']/div[@class='a-section']/form[@name='signIn']/div[@class='a-section']/div[@class='a-box']/div[@class='a-box-inner a-padding-extra-large']/h1").text
driver.quit()
