from hw7.pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    H1_LOCATOR = (By.XPATH, "//h1")

    def check_sign_in_page(self, a_text: str):
        self.verify_element_text(a_text, *self.H1_LOCATOR)