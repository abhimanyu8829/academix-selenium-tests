from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:

    USER_MENU_BUTTONS = (
        By.XPATH,
        "//button | //div[@role='button']"
    )

    LOGOUT_OPTION = (
        By.XPATH,
        "//*[contains(text(),'Logout') or contains(text(),'Sign out')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def logout(self):
        # Step 1: Click the top-right / last menu-like button
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.USER_MENU_BUTTONS)
        )

        # Click the LAST visible button (usually user menu)
        for btn in reversed(buttons):
            try:
                if btn.is_displayed():
                    btn.click()
                    break
            except:
                continue

        # Step 2: Click Logout
        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_OPTION)
        ).click()
