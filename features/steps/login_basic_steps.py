from behave import then

@then("the balance should be greater than zero")
def step_impl(context):
    assert context.ui_balance > 0, f"Balance was {context.ui_balance}"
