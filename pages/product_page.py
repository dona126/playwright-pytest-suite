class ProductPage:
    def __init__(self, page):
        self.page=page

        #Locators
        self.product = page.locator("[data-test='inventory-item']")
         #Filtering locator of first addable product
        self.first_addable_product = page.locator("[data-test='inventory-item']").filter(
            has=page.get_by_role("button", name="Add to cart")).first
        self.product_name = self.first_addable_product.locator(".inventory_item_name")
        self.add_to_cart_btn = self.first_addable_product.get_by_role("button",name="Add to cart")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def product_count_validation(self):
       return self.product

    def add_to_cart(self):
        self.add_to_cart_btn.click()

    def get_cart_badge(self):
        return self.cart_badge
    
    def cart_badge_count(self):
        if self.cart_badge.count() == 0:
            return 0               # ✅ return 0 when badge not visible. Badge will not be in DOM when empty → error
        return int(self.cart_badge.inner_text())

    def product_title_visibility(self):
        return self.product_name
    
    def get_product_title_by_name(self, name):
        return self.page.locator(".inventory_item_name", has_text=name)
    
    def go_to_cart(self):
        self.cart_badge.click()
