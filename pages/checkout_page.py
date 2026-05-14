class CheckoutPage:
    def __init__(self, page):
        self.page = page

        # Locators
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.locator("[data-test='continue']")
        self.finish_btn = page.locator("[data-test='finish']")
        self.confirm_header = page.locator(".complete-header")
        self.error = page.locator("[data-test='error']")

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_btn.click()

    def click_finish(self):
        self.finish_btn.click()

    def get_confirm_header(self):
        return self.confirm_header

    def get_error(self):
        return self.error