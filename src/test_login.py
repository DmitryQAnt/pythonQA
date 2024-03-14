from src.pages.login_page import LoginPage
from src.base_test import BaseTest
from src.utilities.test_data import TestData


class TestLogin(BaseTest):
    def test_login_fail(self, initialize_driver):
        login_page = LoginPage(initialize_driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_authorization_button()
        