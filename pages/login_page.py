from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    LOGIN_ID_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def enter_login_id(self, login_id):
        field = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_ID_INPUT)
        )
        field.clear()
        field.send_keys(login_id)

    def enter_password(self, password):
        field = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
