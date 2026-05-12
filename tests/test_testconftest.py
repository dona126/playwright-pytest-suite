
from playwright.sync_api import expect

def test_login_lands_on_inventory(logged_in_page):
    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

def test_inventory_has_six_products(logged_in_page):
    items = logged_in_page.locator(".inventory_item")
    expect(items).to_have_count(6)

def test_logged_in_page_title(logged_in_page):
    expect(logged_in_page.locator("[data-test='title']")).to_have_text("Products")

