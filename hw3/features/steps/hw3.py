from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HELP_BUTTON_LOCATOR = (By.XPATH, "//li[@class='nav_last']/a[@class='nav_a'][text()='Help']")
SEARCH_FIELD_LOCATOR = (By.XPATH ,"//div[@class='a-column a-span10']//div['a-row']//input[@class='a-input-text a-span12']")
GO_BUTTON_LOCATOR = (By.XPATH ,"//div[@class='a-column a-span2 a-span-last']//span[@class='a-button a-button-span12 a-button-base a-button-dark']//input[@class='a-button-input']")
H1_LOCATOR = (By.XPATH, "//div[@class='a-box a-spacing-extra-large a-color-offset-background answer-box']//div[@class='help-content']//h1[text()='Cancel Items or Orders']")
SHOPPING_CARD_LINK_LOCATOR = (By.XPATH, "//a[@id='nav-cart']")
EMPTY_SHOPPING_CARD_LOCATOR = (By.XPATH, "//h1")
AMAZON_SEARCH_FIELD_LOCATOR = (By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input")
AMAZON_GO_SEARCH_BUTTON = (By.CSS_SELECTOR, "input.nav-input")
AMAZON_SEARCH_SECOND_RESULT = (By.XPATH, "//div[@data-index='3']//a[@class='a-link-normal a-text-normal']")
ADD_TO_CARD_BUTTON_LOCATOR = (By.CSS_SELECTOR, "input.a-button-input.attach-dss-atc")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//span[@class='a-size-small sc-action-delete']//input")
NO_PROTECTION_BUTTON_LOCATOR = (By.CSS_SELECTOR, "span#attachSiNoCoverage.a-button")

@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(4)

@then('Click help button')
def click_help_button(context):
    help_button = context.driver.find_element(*HELP_BUTTON_LOCATOR)
    help_button.click()
    sleep(2)

@then('Open shopping card')
def click_shopping_on_card(context):
    card_button = context.driver.find_element(*SHOPPING_CARD_LINK_LOCATOR)
    card_button.click()
    sleep(2)

@when('Click Amazon Search button')
def click_search_button(context):
    go_button = context.driver.find_element(*AMAZON_GO_SEARCH_BUTTON)
    go_button.click()
    sleep(5)

@when('Input {search_text} into help search field')
def input_into_field(context, search_text):
    search_field = context.driver.find_element(*SEARCH_FIELD_LOCATOR)
    search_field.clear()
    search_field.send_keys(search_text)
    sleep(2)

@when('Input {search_text} into amazon search field')
def input_into_field(context, search_text):
    search_field = context.driver.find_element(*AMAZON_SEARCH_FIELD_LOCATOR)
    search_field.clear()
    search_field.send_keys(search_text)
    sleep(2)

@then('Click on help search icon')
def click_help_search_icon(context):
    go_button = context.driver.find_element(*GO_BUTTON_LOCATOR)
    go_button.click()

@then('Header check for {search_text}')
def check_header1(context, search_text):
    assert search_text in context.driver.find_element(*H1_LOCATOR).text

@then('Check if shopping card is empty')
def check_empty_shopping_card(context):
    assert "Your Shopping Cart is empty." in context.driver.find_element(*EMPTY_SHOPPING_CARD_LOCATOR).text


# Homework 3

@then('Add second item to card')
def add_second_item(context):
    second_item = context.driver.find_element(*AMAZON_SEARCH_SECOND_RESULT)
    second_item.click()

@then('No Protection Plan')
def no_protection(context):
    dis_protection_plan = context.driver.find_element(*NO_PROTECTION_BUTTON_LOCATOR)
    dis_protection_plan.click()

@then('Click add to card')
def add_to_card(context):
    add_to_card_button = context.driver.find_element(*ADD_TO_CARD_BUTTON_LOCATOR)
    add_to_card_button.click()
    sleep(4)

@then('Delete item')
def delete_item(context):
    delete_item_button = context.driver.find_element(*DELETE_BUTTON_LOCATOR)
    delete_item_button.click()
    sleep(4)