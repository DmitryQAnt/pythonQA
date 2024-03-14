from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestLogin(BaseTest):
    def test_login_fail(self, initialize_driver):
        login_page = LoginPage(initialize_driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_authorization_button()
        