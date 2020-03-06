from behave import given, when
from selenium.webdriver.common.by import By

@given('Open Amazon page')
def open_main_page(context):
    context.app.main_page.open()

@when('Click Amazon Orders link')
def click_orders(context):
    context.app.main_page.click_orders()

@when('Click on cart icon')
def click_cart(context):
    context.app.main_page.click_cart()