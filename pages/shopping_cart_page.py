from time import sleep

from pages.BasePage import BasePage
class shopping_cart_page(BasePage):
    def getshopping_cart_URL(self):
        sleep(2)
        expected = "https://www.saucedemo.com/cart.html"
        actual = self.driver.current_url
        assert expected == actual ,'URL diferit'