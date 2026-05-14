class CartPage:
    def __init__(self, page):
        self.page=page

        #Locators
        self.cart_items =  page.locator("[data-test='inventory-item']")
        self.cart_items_names = page.locator("[data-test='inventory-item-name']") #locator to target item names specifically
        self.cart_badge= page.locator("[data-test='shopping-cart-badge']")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.checkout_btn = page.get_by_role("button", name="Checkout")

    def get_cart_items_names(self):
        return self.cart_items_names

    def remove_item(self, name):
        self.cart_items.filter(has_text = name).get_by_role("button", name="Remove").click()

    def get_item_removed(self, name):
        return self.cart_items.filter(has_text=name)
    
    def get_cart_badge(self):
        return self.cart_badge
    
    def get_continue_shopping_button(self):
        return self.continue_shopping_button
    
    def go_to_checkout(self):
        self.checkout_btn.click()




     