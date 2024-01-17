from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3')

    def go_to_login_page(self):
        self.driver.get('https://www.saucedemo.com/')
    def set_user_name(self, user_name):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user_name)
    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    def display_error_message(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None'  # Elementul nu exista pe pagina
        assert actual_message == expected_message, \
            f"Error, message is incorrect,expected {expected_message}, actual {actual_message}"
