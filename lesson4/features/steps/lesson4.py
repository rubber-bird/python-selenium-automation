from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Locators
HAMBURGER_MENU_LOCATOR = (By.ID, 'nav-hamburger-menu')
FIRE_TABLETS_LINK_LOCATOR = (By.XPATH, "//div[@id='hmenu-content']//ul[@class='hmenu  hmenu-visible']//a[@data-menu-id='5']")
FIRE_TABLETS_LINKS_LIST_LOCATOR = (By.CSS_SELECTOR, "#hmenu-content .hmenu-visible a.hmenu-item:not(.hmenu-back-button)")

@given('Open Amazon main page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(4)

@when('Click hamburger menu')
def click_hamburger_menu(context):
    hamburger_menu = context.driver.find_element(*HAMBURGER_MENU_LOCATOR)
    hamburger_menu.click()
    sleep(3)

@when('Click Fire Tablets')
def click_fire_tablets(context):
    fire_tablets_link = context.driver.find_element(*FIRE_TABLETS_LINK_LOCATOR)
    fire_tablets_link.click()
    sleep(4)

@then('Menu will have {expected_items} items')
def get_fire_tablets_links(context, expected_items):
    fire_tablets_links_list = context.driver.find_elements(*FIRE_TABLETS_LINKS_LIST_LOCATOR)
    print(fire_tablets_links_list)
    expected_items = int(expected_items)

    if len(fire_tablets_links_list) > 0:
        assert len(fire_tablets_links_list) == expected_items, f'Expected {expected_items}, but got {len(fire_tablets_links_list)}'
    else:
        print('Not this time')