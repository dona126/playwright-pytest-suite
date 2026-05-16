import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env file

password = os.getenv("SAUCE_PASSWORD")
BASE_URL = os.getenv("BASE_URL")


# browser, context, page → handled by pytest-playwright plugin ✅
# we only write what plugin cannot do → like logged_in_page


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.navigate(BASE_URL)  
    yield login
# Pytest pauses at yield,
# gives object to test,
# then after test finishes it continues below yield.


@pytest.fixture
def product_page(logged_in_page):# logged_in_page runs FIRST
    product = ProductPage(logged_in_page)  # object created AFTER login
    yield product


@pytest.fixture
def cart_page(logged_in_page):# logged_in_page runs FIRST
    cart = CartPage(logged_in_page)  # object created AFTER login
    yield cart

@pytest.fixture
def checkout_page(logged_in_page):
    checkout = CheckoutPage(logged_in_page)
    yield checkout

@pytest.fixture
def logged_in_page(page):        # page comes from plugin
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")# Explicit wait
    # Because Playwright already has auto-waiting.But after:login,navigation,redirects,page changes explicit waits like: 
    # wait_for_url()make tests more stable and clear.
    yield page                   # test gets already logged in page