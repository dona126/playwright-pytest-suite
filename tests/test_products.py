#Test case count: 5

import pytest
from playwright.sync_api import Page, expect

def test_inventory_displays_six_products(product_page):
    """Verify exactly 6 products are displayed on the inventory page"""
    expect(product_page.product_count_validation()).to_have_count(6)


def test_cart_is_empty_before_adding_item(product_page):
    """Verify cart badge is not visible when no items are added"""
    expect(product_page.get_cart_badge()).to_have_count(0)



def test_cart_badge_shows_one_after_single_add(product_page):
    """Verify cart badge shows 1 after adding one item to empty cart"""
    expect(product_page.get_cart_badge()).to_have_count(0)
    product_page.add_to_cart()
    count_after = product_page.get_cart_badge()
    expect(count_after).to_have_text("1")


def test_cart_badge_increments_on_multiple_additions(product_page):
    """Verify cart badge count increments correctly after adding two items"""
    count_before = product_page.cart_badge_count()
    product_page.add_to_cart()
    product_page.add_to_cart()
    expect(product_page.get_cart_badge()).to_have_text(str(count_before+2))


def test_product_title_remains_visible_after_add(product_page):
    """Verify product title is still visible on inventory page after adding item to cart"""
    product_title = product_page.product_title_visibility().inner_text()
    product_page.add_to_cart()
    expect(product_page.get_product_title_by_name(product_title)).to_be_visible()