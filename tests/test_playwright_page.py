

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_playwright_page(driver):
    driver.get("https://playwright.dev/")
    myElement = driver.find_element(By.TAG_NAME, "h1")
    print (f"myElement: {myElement}")
    myElements = driver.find_elements(By.TAG_NAME, "h1")
    print (f"myElements: {myElements}")
    githubElement = driver.find_element(By.CSS_SELECTOR, ".github-btn.github-stargazers.github-btn-large .gh-btn .gh-text")
    print (f"githubElement: {githubElement}")
    # משימת בית
    # element2 = driver.find_element(By.XPATH, )

def test_print_CLI_button(driver):
    driver.get("https://playwright.dev/")
    cliLink = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/nav/div[1]/div[1]/a[4]"))
    )
    print(f"cliLink: {cliLink}")
    cliLink.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("https://playwright.dev/agent-cli/introduction"))
    assert driver.current_url == "https://playwright.dev/agent-cli/introduction"    

