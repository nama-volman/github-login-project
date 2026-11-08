from playwright.sync_api import Page

class BasePage:
    URL = "/"

    def __init__(self, page: Page) -> None:
        self.page = page


    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")