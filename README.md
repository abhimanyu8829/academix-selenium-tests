# Academix Student Portal – Selenium Automation

This project provides automated end-to-end testing for the Academix Student Portal using Python, Selenium, and Pytest.

## Features
- **Login Tests**: Verifies student authentication.
- **Attendance Submission**: Automatically navigates through subjects and submits manual attendance.
- **Page Object Model (POM)**: Organized for maintainability and scalability.
- **Robust Locators**: Uses precise but flexible XPaths to handle dynamic UI elements.
- **Retry Logic**: Handles potential UI state issues during long-running tests.

## Prerequisites
- Python 3.x
- Google Chrome Browser
- ChromeDriver (managed automatically via `webdriver-manager`)

## Setup

1. **Clone the repository** (or navigate to the project directory).
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Unix/macOS**:
     ```bash
     source venv/bin/activate
     ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Update `config/config.py` with your test credentials:
```python
BASE_URL = "https://studentdev.theacademix.com/"
LOGIN_ID = "YOUR_LOGIN_ID"
PASSWORD = "YOUR_PASSWORD"
```

## Running Tests

To run all tests:
```bash
pytest
```

To run specifically the attendance submission tests with console output:
```bash
pytest tests/test_submit_attendance.py -v -s
```

## Project Structure
- `pages/`: Contains Page Object classes (e.g., `attendance_page.py`, `dashboard_page.py`).
- `tests/`: Contains the actual test scripts (e.g., `test_submit_attendance.py`).
- `config/`: Configuration files for URLs and credentials.
- `conftest.py`: Shared pytest fixtures (e.g., `driver` setup).
- `.gitignore`: Excludes environment files and caches from Git.

## Recent Fixes
- Added wait times for JavaScript UI rendering on login and transitions.
- Fixed navigation flow to account for redirect to `/profile` instead of direct dashboard.
- Implemented robust modal interaction for "Manual" attendance submission.
- Added stale element handling and state recovery in test flows.
