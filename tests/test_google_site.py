import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_google_title(driver):
    print (f"Driver: {driver}")
    assert driver.title == "Google"

@pytest.mark.selenium
def test_google_search(driver):
    # search_field = driver.find_element(By.ID, "ti6dpd")
    search_field = driver.find_element(By.NAME, "q")
    search_field.send_keys("SOXL stock price")
    search_field.clear()
    print(f"Attribute: {search_field.get_attribute("name")}")
    print(f"Attribute: {search_field.get_attribute("aria-label")}")
    # search_field.submit()
    search_field.send_keys(Keys.ENTER)
    

