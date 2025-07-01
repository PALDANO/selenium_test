from helpers.ui_helpers import login_ui, go_to_casino, toggle_favorite, find_game_card

def test_favorite_toggle_live_blackjack(driver, test_user):
    login_ui(driver, test_user["username"], test_user["password"])

    try:
        go_to_casino(driver, lang="de")
    except:
        go_to_casino(driver, lang="en")

    game_name = "Live Blackjack"
    game_card = find_game_card(driver, game_name)
    assert game_card is not None, f"Game '{game_name}' not found"

    assert toggle_favorite(driver, game_name, should_be_filled=True), "Favorite not marked"
    assert not toggle_favorite(driver, game_name, should_be_filled=False), "Favorite not unmarked"
