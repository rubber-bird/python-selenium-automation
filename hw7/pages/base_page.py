from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, text: str, *locator):
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def verify_element_count(self, expected_value: int, *locator):
        actual_value = int(len(self.driver.find_elements(*locator)))
        assert actual_value != expected_value, f'Expected {expected_value} elements, but got {actual_value} elements'

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text != expected_text, f'Expected {expected_text} text, but got {actual_text} text'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_located(self, *locator):
        self.driver.wait.until(EC.visibility_of_all_elements_located(locator))