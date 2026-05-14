#Test case count: 5

import pytest
from playwright.sync_api import Page, expect

def test_added_item_visible_in_cart(product_page, cart_page):
    """Verify added item appears in cart page after clicking cart icon"""
    product_title = product_page.product_title_visibility().inner_text()
    product_page.add_to_cart()
    product_page.go_to_cart()
    expect(cart_page.get_cart_items_names()).to_have_text(product_title)


def test_cart_page_url_is_correct(product_page, cart_page):
    """Verify navigating to cart loads correct URL /cart.html"""
    product_page.go_to_cart()
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html") # page becomes a property of cart_page


def test_item_removed_from_cart_successfully(product_page, cart_page):
    """Verify item is removed from cart after clicking remove button"""
    #Verifying add to cart
    product_title = product_page.product_title_visibility().inner_text()
    product_page.add_to_cart()
    product_page.go_to_cart()
    expect(cart_page.get_cart_items_names()).to_have_text(product_title)

    #Verifying remove from cart
    cart_page.remove_item(product_title)
    expect(cart_page.get_item_removed(product_title)).to_have_count(0)


def test_cart_badge_decrements_after_item_removal(product_page, cart_page):
    """Verify cart badge count decrements after removing item from cart"""
    product_title = product_page.product_title_visibility().inner_text()
    product_page.add_to_cart()
    product_page.go_to_cart()
    expect(cart_page.get_cart_items_names()).to_have_text(product_title)
    cart_page.remove_item(product_title)
    expect(cart_page.get_cart_badge()).to_have_count(0)


def test_continue_shopping_button_visible_in_cart(product_page, cart_page):
    """Verify continue shopping button is visible on cart page"""
    product_page.go_to_cart()
    expect(cart_page.get_continue_shopping_button()).to_be_visible()

