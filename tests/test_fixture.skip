@pytest.fixture
def page():
     # 1️⃣ SETUP — runs before test
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()

        yield pg            # 2️⃣ test runs here, receives pg

        browser.close()     # 3️⃣ TEARDOWN — runs after test

def test_login(page):       # page appears automatically
    page.goto("https://saucedemo.com")

def test_products(page):    # same fixture, fresh page
    page.goto("https://saucedemo.com")

# You never call the fixture yourself. 
# PyTest sees the parameter name → matches it → runs it → passes the value in. 
# Same idea as extends BaseTest in Java TestNG — but no import needed.