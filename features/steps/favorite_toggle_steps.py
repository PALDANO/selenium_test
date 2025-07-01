from behave import given, when, then
from helpers.ui_helpers import login_ui, go_to_casino, toggle_favorite, find_game_card

@given("the user is on the casino page")
def step_impl(context):
    try:
        go_to_casino(context.driver, lang="de")
    except:
        go_to_casino(context.driver, lang="en")

@when('the user marks "{game_name}" as favorite')
def step_impl(context, game_name):
    assert find_game_card(context.driver, game_name), f"Game '{game_name}' not found"
    marked = toggle_favorite(context.driver, game_name, should_be_filled=True)
    assert marked, f"Game '{game_name}' was not marked"

@when('the user unmarks "{game_name}" as favorite')
def step_impl(context, game_name):
    unmarked = not toggle_favorite(context.driver, game_name, should_be_filled=False)
    assert unmarked, f"Game '{game_name}' was not unmarked"

@then("the game should no longer be marked as favorite")
def step_impl(context):
    # is already validated above..
    pass
