from playwright.sync_api import Page, expect
from pages.login_github import LoginPage


def test_sign_in_to_gmail(page: Page):
    signInPage = LoginPage(page)
    page.pause()
    signInPage.open()
    signInPage.click_sign_in_button()
    signInPage.fill_credentials()
    expect(signInPage.submit_login_button()).to_be_visible()
    signInPage.click_submit_login()
    