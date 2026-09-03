import pytest
from playwright.sync_api import Page

from POM.Login_page import loging_page
from POM.config import users, username, password


@pytest.mark.parametrize("user", users)
def test_multiplelogin(page:Page, user):
    page.goto("https://www.saucedemo.com/")
    loginpage = loging_page(page)
    loginpage.login(
        user["username"],
        user["password"]
    )




