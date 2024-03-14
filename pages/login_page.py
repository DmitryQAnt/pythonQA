from pages.base_page import BasePage
from pages.my_account_page import MyAccountPage
from utilities.locators import NewUserRegistrationFields

class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email_address):
        # self.set(self.email_address_field, email_address)
        self.driver.find_element(*NewUserRegistrationFields.email_address_field).send_keys(email_address)

    def set_password(self, password):
        self.driver.find_element(*NewUserRegistrationFields.password_field).send_keys(password)

    def click_login_button(self):
        self.click(*NewUserRegistrationFields.login_button)
        return MyAccountPage(self.driver)

    def click_authorization_button(self):
        self.click(*NewUserRegistrationFields.authorization_button)

    def log_into_application(self, email, password):
        self.set_email_address(email)
        self.set_password(password)
        self.click_login_button()

    def get_warning_message(self):
        return self.get_text(*NewUserRegistrationFields.warning_message)

    def execute_script(self, param):
        pass