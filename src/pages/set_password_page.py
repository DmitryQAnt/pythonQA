from src.pages.base_page import BasePage
from src.pages.my_account_page import MyAccountPage
from src.utilities.locators import NewUserRegistrationFields


class SetPasswordPage(BasePage):

    def __init__(self, driver):
        self.locate = NewUserRegistrationFields
        super().__init__(driver)

    def create_new_user(self, first_name, last_name, user_name, password):
        self.set(self.locate.first_name_field, first_name)
        self.set(self.locate.last_name_field, last_name)
        self.set(self.locate.user_name_field, user_name)
        self.set(self.locate.password_field, password)
        self.click(self.locate.capcha_button)
        self.click(self.locate.register_button)
        return MyAccountPage(self.driver)

    def get_confirmation_create_user(self):
        return self.get_text(self.locate.warning_message)
