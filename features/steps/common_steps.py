from behave import given,when
from helpers.ui_helpers import login_ui,get_displayed_balance

@given("the user is logged in")
def step_impl(context):
    login_ui(context.driver, context.username, context.password)

@when("the user checks the balance on the UI")
def step_impl(context):
    context.ui_balance = get_displayed_balance(context.driver) 