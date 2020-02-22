from selenium.webdriver.common.by import By
from behave import given, when, then

COLORS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name ul[role='radiogroup'] li")
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon dress page')
def open_dress_page(context):
    context.driver.get('https://www.amazon.com/dp/B07W36XZ8V/ref=twister_B01M6A0OJ2')

@when('Get all dress colors')
def get_all_dress_colors(context):
    context.dress_colors = context.driver.find_elements(*COLORS_BUTTON_LOCATOR)

@then('Check every color has description')
def color_has_description(context):
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for dress_color in context.dress_colors:
        dress_color.click()
        print(color_title.text)
        print(dress_color.get_attribute('title'))
        assert color_title.text in dress_color.get_attribute('title'), f"Expected {color_title.text} in {dress_color.get_attribute('title')}"
