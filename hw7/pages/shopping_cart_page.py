from hw7.pages.base_page import Page
from selenium.webdriver.common.by import By

class Shopping_cart_page(Page):
    H2_LOCATOR = (By.XPATH, "//h2")

    def verify_empty_cart(self, text: str):
        self.verify_element_text(text, *self.H2_LOCATOR)