import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--lang=en-US")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    print(f"Driver: {driver}")
    yield driver
    driver.quit()  # runs even if the test fails