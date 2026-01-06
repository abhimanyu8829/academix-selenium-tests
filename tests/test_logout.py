import time
from config.config import BASE_URL, LOGIN_ID, PASSWORD
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

def test_logout(driver):
    driver.get(BASE_URL)
    time.sleep(2)

    login = LoginPage(driver)
    login.enter_login_id(LOGIN_ID)
    login.enter_password(PASSWORD)
    login.click_login()

    time.sleep(6)  # ensure dashboard fully loads

    try:
        logout = LogoutPage(driver)
        logout.logout()
    except Exception:
        driver.save_screenshot("logout_failure.png")
        raise

    assert "sign-in" in driver.current_url.lower()
