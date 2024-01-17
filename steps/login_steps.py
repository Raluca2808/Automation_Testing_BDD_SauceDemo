from behave import *

@given('login: I am an user on the login page')
def step_impl(context):
    context.login_page.go_to_login_page()

@when('login: I fill the username with value "{user}"')
def step_impl(context, user):
    context.login_page.set_user_name(user)

@when('login: I fill the password with value "{pwd}"')
def step_impl(context, pwd):
    context.login_page.set_password(pwd)

@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('login: Error message is displayed with the message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.display_error_message(error_message)

@then('inventory: The URL has changed')
def step_impl(context):
    context.inventory_page.getinventory_pageURL()
