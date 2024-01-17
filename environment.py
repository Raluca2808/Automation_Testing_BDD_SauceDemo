from browser import Browser
from pages.login_page import LoginPage
from pages.inventory_page import inventory_page
from pages.BasePage import BasePage
from pages.shopping_cart_page import shopping_cart_page

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.inventory_page = inventory_page()
    context.BasePage = BasePage()
    context.shopping_cart_page = shopping_cart_page()

def after_all(context):
    context.browser.close()