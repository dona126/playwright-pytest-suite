import pytest
from pages.login_page import LoginPage


BASE_URL = "https://www.saucedemo.com"

# browser, context, page → handled by pytest-playwright plugin ✅
# we only write what plugin cannot do → logged_in_page

#used everywhere
@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)  
    yield login
# Pytest pauses at yield,
# gives object to test,
# then after test finishes it continues below yield.

#used in test_testconftest.py file ALONE
@pytest.fixture
def logged_in_page(page):        # page comes from plugin
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")# Explicit wait
    # Because Playwright already has auto-waiting.But after:login,navigation,redirects,page changes explicit waits like: 
    # wait_for_url()make tests more stable and clear.
    yield page                   # test gets already logged in page