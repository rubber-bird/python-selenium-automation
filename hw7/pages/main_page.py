from hw7.pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    AMAZON_ORDERS_LOCATOR = (By.ID, "nav-orders")
    AMAZON_CART_ICON_LOCATOR = (By.ID, "nav-cart")

    def open(self):
        self.open_page('https://www.amazon.com/')

    def click_orders(self):
        self.click(*self.AMAZON_ORDERS_LOCATOR)

    def click_cart(self):
        self.click(*self.AMAZON_CART_ICON_LOCATOR)

