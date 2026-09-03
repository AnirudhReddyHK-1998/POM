import time

from playwright.sync_api import Page, expect




class loging_page:
    def __init__(self, page:Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")
        self.email = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.email.fill(username)
        self.password.fill(password)

        self.login_button.click()

