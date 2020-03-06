from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

BLOG_LINK_LOCATOR = (By.XPATH, "//a[text()='Learn more at blog.aboutamazon.com']")
ADD_TO_CARD_BUTTON_LOCATOR = (By.XPATH, "//input[@id='add-to-cart-button']")
PRODUCT_PAGE_LOCATOR = (By.CSS_SELECTOR, "div.a-section.feed-carousel-viewport li.feed-carousel-card")

@given('Open Amazon page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(5)

@when('Store original windows')
def store_original_window(context):
    context.init_window = context.driver.current_window_handle

@when('Click to blog link')
def click_to_blog_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog_link.click()
    context.all_windows = context.driver.window_handles
    sleep(6)

@when('Switch to the window {window_num}')
def switch_new_window(context, window_num):
    context.driver.switch_to_window(context.all_windows[int(window_num)])
    sleep(5)

@then('Open product page')
def open_page(context):
    context.driver.find_elements(*PRODUCT_PAGE_LOCATOR)[0].click()
    sleep(4)

@then('Add item to card')
def add_to_card(context):
    add_to_card_button = context.driver.find_element(*ADD_TO_CARD_BUTTON_LOCATOR)
    add_to_card_button.click()
    sleep(2)
    try:
        ee = context.driver.find_elements(By.CSS_SELECTOR, "span.a-button")
        if len(ee) > 0:
            ee[1].click()

    except NoSuchElementException:
        print("No Popup Windows:D")

@then('User can close new window and switch back to original')
def go_back_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.init_window)
    sleep(2)

@then('Refresh the page')
def refresh_page(context):
    context.driver.refresh()

@then('Verify that card has {num} item')
def verify_card(context, num):
    if int(context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").text) > int(num):
        print("More than {num}")