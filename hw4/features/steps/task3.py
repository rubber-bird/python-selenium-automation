from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON = (By.CSS_SELECTOR, ".card")

@given('Open Amazon Prime Page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(4)

@then('Check if there are 4 boxes')
def checking(context):
    page = context.driver.find_elements(*AMAZON)
    if len(page) == 4:
        print("There are 4 boxes")
    else:
        print("Sorry")
