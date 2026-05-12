class LoginPage:
    def __init__(self, page):
        self.page = page

        #Locators
        self.username = page.get_by_placeholder("Username")
        self.password =  page.get_by_placeholder("Password")
        self.login_button =  page.get_by_role("button", name = "Login")
        self.error = page.locator("[data-test='error']")
        self.title = page.locator(".login_logo")


    def navigate(self, URL):
        self.page.goto(URL)

    def page_title(self):
        return self.title

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def get_error(self):
        return self.error
