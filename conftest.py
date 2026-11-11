import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI")==True:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    print(f"Driver: {driver}")
    yield driver
    driver.quit()  # runs even if the test fails