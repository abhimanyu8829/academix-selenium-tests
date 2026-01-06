from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # enable for CI

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()
