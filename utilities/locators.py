from selenium.webdriver.common.by import By

class NewUserRegistrationFields:
    first_name_field = (By.ID, "firstname")
    last_name_field = (By.ID, "lastname")
    user_name_field = (By.ID, "userName")
    capcha_button = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    register_button = (By.ID, "register")
    warning_message = (By.ID, "name")

    email_address_field = (By.XPATH, "//input[@type='text' and @name='name']")
    password_field = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    authorization_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']")