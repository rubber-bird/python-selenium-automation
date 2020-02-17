from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Locators
AMAZON_SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input")
AMAZON_GO_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.nav-input")
RESULT_LIST_LOCATOR = (By.CSS_SELECTOR, ".s-result-item")
RESULT_PRICE_LOCATOR = (By.CSS_SELECTOR, ".a-price-whole")
A_LOCATOR = (By.CSS_SELECTOR, ".a-link-normal.a-text-normal")
ADD_TO_CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input#add-to-cart-button")


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

@then('Count Results')
def counting_result(context):
    result_list = context.driver.find_elements(*RESULT_LIST_LOCATOR)
    res = len(result_list)
    print(res)
    sleep(4)

@then('If price of fist element more than 10 dollards add to card')
def add_to_card(context):
    #result_list = context.driver.find_elements(*RESULT_LIST_LOCATOR)
    first_res = context.driver.find_elements(*RESULT_LIST_LOCATOR)[0]
    first_res_price = first_res.find_element(*RESULT_PRICE_LOCATOR).text
    first_res_element = first_res.find_element(*A_LOCATOR)
    sleep(3)
    if int(first_res_price) > 10:
        first_res_element.click()
        add_to_card_button = context.driver.find_element(*ADD_TO_CARD_BUTTON_LOCATOR)
        add_to_card_button.click()
        sleep(4)
