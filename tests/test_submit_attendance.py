from config.config import BASE_URL, LOGIN_ID, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.attendance_page import AttendancePage
import time


def submit_attendance_flow(driver, mode):
    attendance = AttendancePage(driver)
    attendance.open_attendance()

    items = attendance.get_items()


    for i in range(len(items)):
        # Refetch items to avoid stale elements
        current_items = attendance.get_items()
        if i >= len(current_items):
            break
        
        item = current_items[i]
        try:
            # Click on the subject card
            print(f"DEBUG: Trying item {i+1}: {item.text}")
            driver.execute_script("arguments[0].scrollIntoView(true);", item)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", item)
            time.sleep(3)  # Wait for calendar page
            
            # Click "Submit Attendance" button
            print("DEBUG: Clicking Submit Attendance button")
            attendance.open_submit_modal()
            
            # Select "Manual" in the modal
            print("DEBUG: Selecting Manual option")
            attendance.select_manual_attendance()

            # Click "Submit" in the modal
            print("DEBUG: Clicking Submit button in modal")
            attendance.submit()
            time.sleep(3)  # Wait for submission
            
            print("DEBUG: Submission completed")
            return
        except Exception as e:
            print(f"DEBUG: Failed for item {i+1}, trying next. Error: {e}")
            driver.get(driver.current_url.split('/attendance')[0] + '/attendance') # Reset to attendance page
            time.sleep(2)
            continue




    assert False, "No pending attendance found"


def test_submit_subject_wise_attendance(driver):
    driver.get(BASE_URL)
    time.sleep(3)  # wait for JS UI to render

    login = LoginPage(driver)
    login.enter_login_id(LOGIN_ID)
    login.enter_password(PASSWORD)
    login.click_login()

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    submit_attendance_flow(driver, mode="subject")



def test_submit_class_wise_attendance(driver):
    driver.get(BASE_URL)
    time.sleep(3)  # wait for JS UI to render

    login = LoginPage(driver)
    login.enter_login_id(LOGIN_ID)
    login.enter_password(PASSWORD)
    login.click_login()

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    submit_attendance_flow(driver, mode="class")

