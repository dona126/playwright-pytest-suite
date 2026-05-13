#Test case count: 5
import pytest
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

def test_added_item_visible_in_cart(product_page, cart_page):
    """Verify added item appears in cart page after clicking cart icon"""

def test_cart_page_url_is_correct(product_page):
    """Verify navigating to cart loads correct URL /cart.html"""

def test_item_removed_from_cart_successfully(product_page, cart_page):
    """Verify item is removed from cart after clicking remove button"""

def test_cart_badge_decrements_after_item_removal(product_page, cart_page):
    """Verify cart badge count decrements after removing item from cart"""

def test_continue_shopping_button_visible_in_cart(product_page, cart_page):
    """Verify continue shopping button is visible on cart page"""