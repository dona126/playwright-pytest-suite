#Full login test suite — valid, invalid, locked user, empty fields, parametrize, page title
#Test case count: 6

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")  # call method
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")  # here its products page..tht y page used n not login_page

def test_page_title(login_page):
    expect(login_page.page_title()).to_have_text("Swag Labs")


@pytest.mark.parametrize("username, password, expected_text", [
    ("", "",                     "Epic sadface: Username is required"),
    ("standard_user", "",        "Epic sadface: Password is required"),
    ("wrong_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
])
def test_login_errors(login_page, username, password, expected_text):
    login_page.login(username, password)
    expect(login_page.get_error()).to_have_text(expected_text)
