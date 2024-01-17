from selenium.webdriver.common.by import By

from browser import Browser

class BasePage(Browser):
    USERNAME_INPUT = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def set_user_name(self, user_name):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(user_name)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
