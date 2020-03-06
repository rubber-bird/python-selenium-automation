from behave import then
from selenium.webdriver.common.by import By

@then('Verify {text} page is opened')
def verify_opened_page(context, text):
    context.app.sign_in_page.check_sign_in_page(text)