from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLER_BUTTON = (By.CSS_SELECTOR, ".a-badge-text")
AMAZON_SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input")
AMAZON_GO_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.nav-input")

@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(4)

@when('Input {search_text} into amazon search field')
def input_into_field(context, search_text):
    search_field = context.driver.find_element(*AMAZON_SEARCH_FIELD_LOCATOR)
    search_field.clear()
    search_field.send_keys(search_text)
    sleep(2)

@when('Click Search button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*AMAZON_GO_SEARCH_BUTTON)
    amazon_search_button.click()
    sleep(2)

@then('Count Best sellers')
def count(context):
    list_of_best_seller_elements = context.driver.find_elements(*BEST_SELLER_BUTTON)
    print(len(list_of_best_seller_elements))