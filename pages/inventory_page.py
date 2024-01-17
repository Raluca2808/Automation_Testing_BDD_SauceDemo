from time import sleep

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

class inventory_page(BasePage):
    SETTINGS_BTN = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    LOGO_ICON = (By.CLASS_NAME, 'app_logo')
    SHOPPING_CART_BTN = (By.XPATH, '//a[@class="shopping_cart_link"]')
    FILTER_BTN = (By.XPATH, '//select[@class="product_sort_container"]')
    SETTINGS_LIST = (By.XPATH, '//nav[@class="bm-item-list"]')
    def getinventory_pageURL(self):
        sleep(2)
        expected = "https://www.saucedemo.com/inventory.html"
        actual = self.driver.current_url
        assert expected == actual ,'URL diferit'
    def click_settings_btn(self):
        self.driver.find_element(*self.SETTINGS_BTN).click()
    def check_logo_icon(self):
        actual = self.driver.find_element(*self.LOGO_ICON).is_displayed()
        expected = True
        assert expected == actual, 'Logo is not displayed'
    def click_shopping_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_BTN).click()
    def click_filter_btn(self):
        self.driver.find_element(*self.FILTER_BTN).click()
    def check_settings_list(self):
        actual = self.driver.find_element(*self.SETTINGS_LIST).is_displayed()
        expected = True
        assert expected == actual, 'List is not displyed'