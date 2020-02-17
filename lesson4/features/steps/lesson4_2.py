from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

POPUP_LOCATOR = (By.CSS_SELECTOR, ".otw-popup-content-inner")
POPUP_CLOSE_BUTTON = (By.CSS_SELECTOR, "#otw-overlay-1 .mfp-close")

@given('Open Heritage site')
def open_main_page(context):
    context.driver.get('https://heritagedoorsandwindows.com/')
    sleep(5)

@when('See popup')
def see_popup(context):
    popup = context.driver.find_element(*POPUP_LOCATOR)
    sleep(2)

@then('Close popup')
def close_popup(context):
    popup_close_buttons = context.driver.find_elements(*POPUP_CLOSE_BUTTON)
    print(popup_close_buttons)
    if len(popup_close_buttons) > 0:
        popup_close_buttons[0].click()

