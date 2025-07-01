from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):

    print("test, let's gooooo!")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.username = "petergreener"
    context.password = "qwer1234"

def after_scenario(context, scenario):
    context.driver.quit()
