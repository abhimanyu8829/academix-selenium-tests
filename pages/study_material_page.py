from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class StudyMaterialPage:

    # Class card on profile page
    CLASS_CARD = (By.XPATH, "//div[contains(@class,'card')]//h2 | //h2")

    # ================= LEFT SIDEBAR =================
    STUDY_MATERIAL_MENU = (
        By.XPATH,
        "//span[normalize-space()='Study Materials'] | //a[contains(@href,'study')]"
    )

    # On E-Library page, subjects are often in a dropdown
    SUBJECT_DROPDOWN = (By.XPATH, "//div[@id='demo-select-small'] | //div[contains(@class, 'MuiSelect-select')]")
    SUBJECT_OPTIONS = (By.XPATH, "//li[@role='option'] | //ul[contains(@class, 'MuiList-root')]//li")

    # ================= TOPICS & RESOURCES =================
    TOPIC_ITEMS = (By.XPATH, "//*[contains(@class, 'MuiAccordionSummary-root')] | //div[contains(@class, 'MuiAccordion-root')]")
    RESOURCE_ITEMS = (
        By.XPATH,
        "//p[text()='PDF']/parent::div | //p[text()='Video']/parent::div | //p[text()='Image']/parent::div"
    )

    # ================= VIEWERS =================
    VIDEO_PLAYER = (By.XPATH, "//video")
    PDF_VIEWER = (By.XPATH, "//embed | //iframe[contains(@src,'pdf')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # ================= MAIN FLOW =================

    def open_study_material(self):
        # 1. Click batch card on profile page
        class_card = self.wait.until(
            EC.element_to_be_clickable(self.CLASS_CARD)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", class_card)
        self.driver.execute_script("arguments[0].click();", class_card)
        time.sleep(5)  # Wait for dashboard/sidebar to load

        # 2. Click Study Materials in sidebar
        menu = self.wait.until(
            EC.presence_of_element_located(self.STUDY_MATERIAL_MENU)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", menu)
        self.driver.execute_script("arguments[0].click();", menu)
        time.sleep(4)  # SPA navigation

    def get_subjects(self):
        # Open dropdown first
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SUBJECT_DROPDOWN)
        )
        self.driver.execute_script("arguments[0].click();", dropdown)
        time.sleep(1)
        return self.wait.until(
            EC.presence_of_all_elements_located(self.SUBJECT_OPTIONS)
        )

    def select_subject_by_index(self, index):
        options = self.get_subjects()
        if index < len(options):
            self.driver.execute_script("arguments[0].click();", options[index])
            time.sleep(3)

    def open_resources(self):
        # On E-Library, topics (accordions) might need to be clicked
        topics = self.wait.until(
            EC.presence_of_all_elements_located(self.TOPIC_ITEMS)
        )
        for topic in topics:
            self.driver.execute_script("arguments[0].click();", topic)
            time.sleep(1)

    def get_resources(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.RESOURCE_ITEMS)
        )

    def open_resource(self, resource):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", resource)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", resource)
        time.sleep(3)

    # ================= ASSERTIONS =================

    def is_video_opened(self):
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.VIDEO_PLAYER)
            ).is_displayed()
        except:
            return False

    def is_pdf_opened(self):
        try:
            return self.wait.until(
                EC.presence_of_element_located(self.PDF_VIEWER)
            ).is_displayed()
        except:
            return False
