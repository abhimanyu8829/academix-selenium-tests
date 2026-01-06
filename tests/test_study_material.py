from config.config import BASE_URL, LOGIN_ID, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.study_material_page import StudyMaterialPage
import time


def test_study_material_resources(driver):

    driver.get(BASE_URL)
    time.sleep(3)

    # ================= LOGIN =================
    login = LoginPage(driver)
    login.enter_login_id(LOGIN_ID)
    login.enter_password(PASSWORD)
    login.click_login()

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    study = StudyMaterialPage(driver)

    # ================= STUDY MATERIAL =================
    study.open_study_material()

    # Get number of subjects from dropdown
    subjects = study.get_subjects()
    num_subjects = len(subjects)
    print(f"DEBUG: Found {num_subjects} subjects in dropdown")

    for i in range(num_subjects):
        try:
            print(f"DEBUG: Selecting subject index {i}")
            study.select_subject_by_index(i)
            
            print("DEBUG: Opening topics (accordions)")
            study.open_resources() # This opens the accordions on E-Library

            resources = study.get_resources()
            if not resources:
                print(f"DEBUG: No resources for subject index {i}, trying next.")
                continue

            print(f"DEBUG: Opening first resource from {len(resources)} found")
            study.open_resource(resources[0])

            assert (
                study.is_video_opened() or study.is_pdf_opened()
            ), "Resource opened but no video or PDF detected"

            print("DEBUG: Resource verified successfully")
            return

        except Exception as e:
            print(f"DEBUG: Failed for subject index {i}, retrying. Error: {e}")
            driver.get(driver.current_url)
            time.sleep(3)
            # Re-open study material if we refreshed
            study.open_study_material()
            continue

    assert False, "No valid study material resource found"
