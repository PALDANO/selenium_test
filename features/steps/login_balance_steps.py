from behave import given, when, then
from helpers.api_helpers import login_and_get_token, get_balance

@when("the user checks the balance from the API")
def step_impl(context):
    token = login_and_get_token(context.username, context.password)
    context.api_balance = get_balance(token)
   
@then("both balances should match")
def step_impl(context):
    print(f"🔍 UI Balance: {context.ui_balance}, API Balance: {context.api_balance}")
    assert abs(context.ui_balance - context.api_balance) < 0.01, "Balances don't match"
