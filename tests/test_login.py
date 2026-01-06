from config.config import BASE_URL, LOGIN_ID, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_student_login(driver):
    driver.get(BASE_URL)
    time.sleep(3)  # wait for JS UI to render

    login_page = LoginPage(driver)
    login_page.enter_login_id(LOGIN_ID)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded(), "Dashboard did not load"
