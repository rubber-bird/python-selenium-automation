from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TAB_MENU_LOCATOR = (By.CSS_SELECTOR, "div#zg_tabs li")
HEADER_LOCATOR = (By.XPATH, "//div[@id='zg_banner_text_wrapper']")

@given('Open Amazon Best Sellers page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@when('Get elements from tab menu')
def get_elements(context):
    context.elements = context.driver.find_elements(*TAB_MENU_LOCATOR)


@then('Check each value with header')
def check(context):
    i = 1
    while i != len(context.elements):
    #for element in context.elements:
        next = context.driver.find_elements(*TAB_MENU_LOCATOR)[i]
        temp_header = context.driver.find_element(*HEADER_LOCATOR)
        if temp_header.text.find(next.text) != -1:
            print('ok')
        next.click()
        i += 1

