from selenium.webdriver.common.by import By
import locator

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys()

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title
