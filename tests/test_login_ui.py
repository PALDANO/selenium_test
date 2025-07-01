from helpers.ui_helpers import login_ui, get_displayed_balance

def test_login_and_check_balance(driver, test_user):
    login_ui(driver, test_user["username"], test_user["password"])

    balance = get_displayed_balance(driver)
    print("Logged in. Balance:", balance)
    assert balance > 0
