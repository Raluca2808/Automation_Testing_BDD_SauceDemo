from behave import *
@when('inventory: I click the settings button')
def step_impl(context):
    context.inventory_page.click_settings_btn()

@then('inventory: I am on inventory page')
def step_impl(context):
    context.inventory_page.getinventory_pageURL()

@then('inventory: Settings list is displayed')
def step_impl(context):
    context.inventory_page.check_settings_list()

@then('inventory: logo is displayed')
def step_impl(context):
    context.inventory_page.check_logo_icon()

@then('inventory: I click on the cart icon')
def step_impl(context):
    context.inventory_page.click_shopping_cart()

@then('cart: The URL has changed')
def step_impl(context):
    context.shopping_cart_page.getshopping_cart_URL()
