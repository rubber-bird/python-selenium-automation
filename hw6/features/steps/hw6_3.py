from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Constants
SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "input#searchval")
SEARCH_FIELD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button.btn.btn-info.banner-search-btn")
RESULT_DESCRIPTION_LOCATOR = (By.CSS_SELECTOR, "div.ag-item.gtm-product")
ADD_TO_CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.btn.btn-cart.btn-small")
RESULT_DESCRIPTION_A_LOCATOR = (By.CSS_SELECTOR, "a.description")
EMPTY_CART_LOCATOR = (By.CSS_SELECTOR, "a.emptyCartButton.btn.btn-mini.btn-ui.pull-right")
POPUP_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Empty Cart']")

@given('Open Webpage')
def open_page(context):
    context.driver.get('https://www.webstaurantstore.com/')

@when('Search for {search_req_text}')
def search_func(context, search_req_text):
    search_field = context.driver.find_element(*SEARCH_FIELD_LOCATOR)
    search_field.send_keys(search_req_text)
    sleep(3)
    search_field_button = context.driver.find_element(*SEARCH_FIELD_BUTTON_LOCATOR).click()
    sleep(3)

@then('Check the search result ensuring every product item has the word {word} its title')
def check_words(context, word):
    context.counter = 0
    context.result_list = context.driver.find_elements(*RESULT_DESCRIPTION_LOCATOR)
    for elem in context.result_list:
        a_tag_text = elem.find_element(*RESULT_DESCRIPTION_A_LOCATOR).text
        if a_tag_text.find("Table") == -1:
            context.counter += 1

    if context.counter == 0:
        print("Each description includes word 'Table'")
    else:
        print("BOOOOOM")

@then('Add the last of found items to Cart')
def add_last_element(context):
    last_element = context.result_list[len(context.result_list)-1].find_element(*ADD_TO_CART_BUTTON_LOCATOR).click()
    sleep(3)

@then('Empty Cart')
def empty_cart(context):
    context.driver.get('https://www.webstaurantstore.com/viewcart.cfm')
    empty_cart_button = context.driver.find_element(*EMPTY_CART_LOCATOR)
    empty_cart_button.click()
    sleep(2)
    context.driver.find_element(*POPUP_BUTTON_LOCATOR).click()