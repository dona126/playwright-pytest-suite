import pytest

BASE_URL = "https://www.saucedemo.com"

# browser, context, page → handled by pytest-playwright plugin ✅
# we only write what plugin cannot do → logged_in_page

@pytest.fixture
def logged_in_page(page):        # page comes from plugin
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")
    yield page                   # test gets already logged in page