import time
from config.config import BASE_URL
from pages.login_page import LoginPage

def test_invalid_login(driver):
    driver.get(BASE_URL)
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.enter_login_id("invalid_user")
    login_page.enter_password("wrong_pass")
    login_page.click_login()

    time.sleep(2)

    # Assertion can be improved once error text is known
    assert "sign-in" in driver.current_url.lower()
