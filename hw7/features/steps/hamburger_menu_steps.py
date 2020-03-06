from behave import when, then
from selenium.webdriver.common.by import By

@when('Click on hamburger menu')
def open_hamburger_menu(context):
    context.app.hamburger_menu.click_hamburger_menu()

@when('Click on Amazon Music menu item')
def open_amazon_music(context):
    context.app.hamburger_menu.click_amazon_music()

@then('{val} menu items are present')
def count(context, val):
    context.app.hamburger_menu.hmenu_music_tags_count(val)
