# Test case: 4

from playwright.sync_api import expect

def test_complete_checkout_flow(product_page, cart_page, checkout_page):
    """E2E — Full journey: add item → cart → checkout → confirm order"""
    product_page.add_to_cart()
    expect(product_page.get_cart_badge()).to_have_text("1")

    product_page.go_to_cart()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")

    cart_page.go_to_checkout()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    
    checkout_page.fill_form("Tester", "User", "12345")
    checkout_page.click_continue()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")  

    checkout_page.click_finish()
    expect(product_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_page.get_confirm_header()).to_contain_text("Thank you")
    

def test_checkout_missing_firstname(product_page, cart_page, checkout_page):
    """Verify error shown when first name missing on checkout form"""
    product_page.add_to_cart()
    product_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.click_continue()       # empty form submit
    expect(checkout_page.get_error()).to_contain_text("First Name is required")

def test_checkout_missing_lastname(product_page, cart_page, checkout_page):
    """Verify error shown when last name missing on checkout form"""
    product_page.add_to_cart()
    product_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_form("Tester", "", "12345")
    checkout_page.click_continue()    
    expect(checkout_page.get_error()).to_contain_text("Last Name is required")

def test_checkout_missing_postalcode(product_page, cart_page, checkout_page):
    """Verify error shown when postal code missing on checkout form"""
    product_page.add_to_cart()
    product_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_form("Don", "Tester", "")
    checkout_page.click_continue()
    expect(checkout_page.get_error()).to_contain_text("Postal Code is required")