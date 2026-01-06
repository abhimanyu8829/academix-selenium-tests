from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AttendancePage:

    # Class card on profile page
    CLASS_CARD = (By.XPATH, "//div[contains(@class,'card')]//h2 | //h2")

    ATTENDANCE_TAB = (
        By.XPATH,
        "//span[normalize-space()='Attendance']"
    )

    SUBJECT_WISE_TAB = (By.XPATH, "//button[contains(text(),'Subject')]")
    CLASS_WISE_TAB = (By.XPATH, "//button[contains(text(),'Class')]")

    ATTENDANCE_ITEMS = (
        By.XPATH,
        "//h2 | //div[contains(@class,'card')]//h2 | //div[p[contains(text(), '#')]] | //div[contains(@class, 'subject')]//h2"
    )

    MANUAL_OPTION = (By.XPATH, "//*[contains(text(),'Manual')] | //p[text()='Manual'] | //div[@role='dialog']//*[contains(text(),'Manual')]")
    SUBMIT_ATTENDANCE_BUTTON = (By.XPATH, "//button[contains(.,'Submit Attendance')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Submit'] | //div[@role='dialog']//button[contains(.,'Submit')] | //button[contains(text(),'Submit')]")

    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")

    ALREADY_SUBMITTED_MSG = (
        By.XPATH,
        "//*[contains(text(),'already submitted')]"
    )

    SUCCESS_MSG = (
        By.XPATH,
        "//*[contains(text(),'Attendance') and (contains(text(),'submitted') or contains(text(),'Successfully'))]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # ================== MAIN NAVIGATION ==================

    def open_attendance(self):
        # Click first class card from profile page
        class_card = self.wait.until(
            EC.element_to_be_clickable(self.CLASS_CARD)
        )
        self.driver.execute_script("arguments[0].click();", class_card)

        time.sleep(3)  # Wait for dashboard to load

        # Click Attendance tab
        attendance_tab = self.wait.until(
            EC.element_to_be_clickable(self.ATTENDANCE_TAB)
        )
        self.driver.execute_script("arguments[0].click();", attendance_tab)

        time.sleep(2)  # Wait for attendance page to load

    # ================== ATTENDANCE TYPE ==================

    def select_subject_wise(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SUBJECT_WISE_TAB)
        ).click()
        time.sleep(2)

    def select_class_wise(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CLASS_WISE_TAB)
        ).click()
        time.sleep(2)

    def get_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.ATTENDANCE_ITEMS)
        )

    # ================== SUBMISSION ==================

    def open_submit_modal(self):
        btn = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_ATTENDANCE_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

    def select_manual_attendance(self):
        manual = self.wait.until(
            EC.presence_of_element_located(self.MANUAL_OPTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", manual)
        self.driver.execute_script("arguments[0].click();", manual)
        time.sleep(1)

    def submit(self):
        submit_btn = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def is_successful(self):
        return self.wait.until(
            EC.presence_of_element_located(self.SUCCESS_MSG)
        ).is_displayed()
