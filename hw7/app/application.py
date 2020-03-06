from hw7.pages.main_page import MainPage
from hw7.pages.shopping_cart_page import Shopping_cart_page
from hw7.pages.sign_in_page import SignInPage
from hw7.pages.hamburger_menu import Hamburger_menu

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.shopping_cart_page = Shopping_cart_page(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.hamburger_menu = Hamburger_menu(self.driver)