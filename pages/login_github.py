from playwright.sync_api import Locator , Page
from pages.base_page import BasePage
from utilities import config
import re
import os

class LoginPage(BasePage):
    URL = config.GITHUB_URL

    def __init__(self, page: Page):
        super().__init__(page)

    def click_sign_in_button(self) -> Locator:
        self.sign_in_button().click()
        self.page.wait_for_load_state('domcontentloaded')

    def sign_in_button(self):
        return self.page.get_by_role("link", name="Sign in")

    def fill_credentials(self):
        username = config.DETAILS.get("github_username")
        password = config.DETAILS.get("github_password")
        self.username_textbox().fill(username)
        self.password_textbox().fill(password)

    def username_textbox(self):
        return self.page.get_by_role("textbox", name="Username or email address")
        
    def password_textbox(self):
        return self.page.get_by_label("Password")

    def click_submit_login(self):
        self.submit_login_button().click()

    def submit_login_button(self):
        return self.page.get_by_role("button", name="Sign in" , exact=True)
