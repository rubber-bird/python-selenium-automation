from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PROCESSOR_MODEL_DESC_LOCATOR = (By.CSS_SELECTOR, "#variation_processor_description ul[role='radiogroup'] li")
VARIATION_NAME_LOCATOR = (By.CSS_SELECTOR, "#variation_processor_description .selection")
ADD_TO_CARD_BUTTON_LOCATOR = (By.XPATH, "//input[@id='add-to-cart-button']")
POPOVER_LOCATOR = (By.CSS_SELECTOR, ".a-section.attach-desktop-sideSheet")
POPOVER_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".a-section.attach-warranty-button-row button")
H4_LOCATOR = (By.XPATH, "//h4[@class='a-alert-heading'][text()='Added to Cart']")

@given('Open Amazon laptop page')
def open_dress_page(context):
    context.driver.get('https://www.amazon.com/dp/B07Z11X58J/ref=twister_B082RB7DZH?_encoding=UTF8&psc=1')

@when('Get Processor Description')
def find_processor_variation_list(context):
    context.processor_variation_list = context.driver.find_elements(*PROCESSOR_MODEL_DESC_LOCATOR)

@then('Check Processor Description')
def check_desc(context):
    description_model = context.driver.find_element(*VARIATION_NAME_LOCATOR)
    for description in context.processor_variation_list:
        description.click()
        print(description_model.text)
        print(description.get_attribute('title'))
        assert description_model.text in description.get_attribute('title'), f"Expected {description_model.text} in {description.get_attribute('title')}"

@then('Select {num_choice} choice')
def select_desc(context, num_choice):
    elem = int(num_choice)
    elem += 1
    context.processor_variation_list[1].click()
    sleep(3)

@then('Add to Card')
def add_to_card(context):
    add_to_card_button = context.driver.find_element(*ADD_TO_CARD_BUTTON_LOCATOR)
    add_to_card_button.click()
    sleep(2)

@then('Check for pop up protection plan')
def see_popup(context):
    popover_button = context.driver.find_elements(*POPOVER_BUTTON_LOCATOR)
    if(len(popover_button) > 0):
        popover_button[1].click()

@then('Check the final header')
def check_header(context):
    header = context.driver.find_element(*H4_LOCATOR)
    if header:
        print("Success")
    else:
        print("Failure")