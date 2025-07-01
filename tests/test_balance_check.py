from helpers.ui_helpers import login_ui, get_displayed_balance
from helpers.api_helpers import login_and_get_token, get_balance

def test_ui_balance_matches_api(driver, test_user):
    login_ui(driver, test_user["username"], test_user["password"])
    ui_balance = get_displayed_balance(driver)

    token = login_and_get_token(test_user["username"], test_user["password"])
    api_balance = get_balance(token)

    print(f"UI Balance: {ui_balance}")
    print(f"API Balance: {api_balance}")

    assert abs(ui_balance - api_balance) < 0.01, "UI and API balances do not match!"
