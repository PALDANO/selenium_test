from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Logs into the acc
def login_ui(driver, username, password):
    driver.get("https://www.gametwist.com")
    wait = WebDriverWait(driver, 15)

    login_btn = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "a.c-btn.c-btn--secondary.c-btn--header"
    )))
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.js-confirmLoginModal"))).click()

    try:
        wheel_close = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a.c-wheel__btn-close"
        )))
        wheel_close.click()
    except TimeoutException:
        pass

# Retrieves the displayed balance from the UI
def get_displayed_balance(driver):
    wait = WebDriverWait(driver, 10)
    balance_el = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, "div.c-balance__panel"
    )))
    balance_text = balance_el.text.replace(".", "").replace(",", ".").replace("Twist", "").strip()
    return float(balance_text)



# Navigates to the casino
def go_to_casino(driver, lang="de"):
    driver.get(f"https://www.gametwist.com/{lang}/casino/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.LINK_TEXT, "Live Blackjack"
    )))


# Finds a game by its visible name
def find_game_card(driver, game_name):
    try:
        return driver.find_element(By.LINK_TEXT, game_name)
    except:
        return None

# Toggles favorite icon for a game
def toggle_favorite(driver, game_name, should_be_filled):
    game_title = find_game_card(driver, game_name)
    if not game_title:
        raise Exception(f"Game '{game_name}' not found")

    parent_tile = game_title.find_element(By.XPATH, "../..")
    heart_icon = parent_tile.find_element(By.CSS_SELECTOR, 'a.c-game__fav')

    is_filled = "is-favorite" in heart_icon.get_attribute("class")
    if is_filled != should_be_filled:
        heart_icon.click()
        WebDriverWait(driver, 5).until(lambda d: (
            ("is-favorite" in heart_icon.get_attribute("class")) == should_be_filled
        ))

    return "is-favorite" in heart_icon.get_attribute("class")
