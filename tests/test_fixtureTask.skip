# Write the 3 simple assert tests → run → all pass
#  Write user_creds fixture → 2 tests use it → run → pass
#  Write browser + page fixture chain → test_page_title passes
#  Break one test on purpose → read the failure output → fix it
#  Run all: pytest tests/test_day15.py -v → all 6 green
#  Push with commit message: feat: day15 pytest basics and fixtures

import pytest
from playwright.sync_api import sync_playwright


def test_add():
    assert 5+2 == 7

def test_sub():
    assert "saucedemo".lower() == "saucedemo"

def test_mult():
    assert 5*2 == 10

#............................................
@pytest.fixture
def user_creds():
    yield {
        "username": "standard_user",
        "password": "secret_sauce"
    }

def test_printUsername(user_creds):
    assert user_creds["username"] == "standard_user"

def test_printPassword(user_creds):
     assert user_creds["password"] == "secret_sauce"

#................................................
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch(headless=False)
        yield b
        b.close()

@pytest.fixture
def page(browser):
    pg = browser.new_page()
    pg.goto("https://www.saucedemo.com")
    yield pg
    pg.close()

def test_page_title(page):
    assert "Swag Labs" == page.title()







