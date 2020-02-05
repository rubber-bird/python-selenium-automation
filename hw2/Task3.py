from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='../drivers/chromedriver')

driver.get('https://www.amazon.com/')
sleep(4)
help_button = driver.find_element(By.XPATH, "//div[@class='navFooterVerticalRow navAccessibility']//div[@class='navFooterLinkCol navAccessibility']//li[@class='nav_last']//a[@class='nav_a'][text()='Help']")
help_button.click()
sleep(4)

search = driver.find_element(By.XPATH, "//div[@class='a-row']//div[@class='a-section a-spacing-extra-large a-spacing-top-extra-large ss-landing-container-wide']//div[@class='a-row']//div[@class='a-search a-span12']//input[@class='a-input-text a-span12']")
search_button = driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-large']//div[@class='a-column a-span2 a-span-last']//span[@class='a-button-inner']//input[@class='a-button-input']")

sleep(4)

search.clear()
search.send_keys('cancel order')
search_button.click()

sleep(4)

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large a-color-offset-background answer-box']//div[@class='help-content']//h1").text

driver.quit()