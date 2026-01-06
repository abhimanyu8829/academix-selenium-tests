from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    # After login, the page redirects to /profile which shows "My Learning(s)"
    DASHBOARD_MARKER = (By.XPATH, "//*[contains(text(),'My Learning')]")
    
    # Fallback: check for class cards as alternative
    CLASS_CARDS = (By.XPATH, "//div[contains(@class,'class') or contains(@class,'card')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def is_dashboard_loaded(self):
        # Check for either "My Learning" text or class cards
        try:
            self.wait.until(
                EC.presence_of_element_located(self.DASHBOARD_MARKER)
            )
            return True
        except:
            # Fallback: check if class cards are present
            self.wait.until(
                EC.presence_of_element_located(self.CLASS_CARDS)
            )
            return True
