from hw7.pages.base_page import Page
from selenium.webdriver.common.by import By

class Hamburger_menu(Page):
    HAMBURGER_MENU_LOCATOR = (By.ID, "nav-hamburger-menu")
    AMAZON_MUSIC_LOCATOR = (By.XPATH, "//a[@data-menu-id='3']")
    HMENU_LI_TAGS_LOCATOR = (By.CSS_SELECTOR, "ul.hmenu.hmenu-visible.hmenu-translateX li:not(.hmenu-separator) a:not(.hmenu-back-button)")

    def click_hamburger_menu(self):
        self.wait_for_element_click(*self.HAMBURGER_MENU_LOCATOR)

    def click_amazon_music(self):
        self.wait_for_element_click(*self.AMAZON_MUSIC_LOCATOR)

    def hmenu_music_tags_count(self, val: int):
        self.verify_element_count(val, *self.HMENU_LI_TAGS_LOCATOR)