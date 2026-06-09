# 🧪 Playwright PyTest Suite

Full E2E test suite for [SauceDemo](https://www.saucedemo.com) built with
Playwright, PyTest, and POM — with GitHub Actions CI/CD.

---

## 🛠 Tech Stack

- Python 3.12 · Playwright · PyTest · POM · GitHub Actions

---

## 📁 Project Structure
```
playwright-pytest-suite/
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_product.py
│   ├── test_cart.py
│   └── test_checkout.py
├── .env               ← local only, gitignored
├── requirements.txt
└── README.md
```

---


## Test Cases
 
### Login
| Test | Description |
|------|-------------|
| `test_valid_login` | Valid credentials redirect to inventory page |
| `test_page_title` | Login page displays correct title |
| `test_login_errors[4]` | Invalid, empty, locked credentials show correct errors |
 
### Product
| Test | Description |
|------|-------------|
| `test_inventory_displays_six_products` | Inventory displays exactly 6 products |
| `test_cart_is_empty_before_adding_item` | Cart badge not visible before adding any item |
| `test_cart_badge_shows_one_after_single_add` | Cart badge shows 1 after adding one item |
| `test_cart_badge_increments_on_multiple_additions` | Cart badge increments after adding two items |
| `test_product_title_remains_visible_after_add` | Product title remains visible after add to cart |
 
### Cart
| Test | Description |
|------|-------------|
| `test_added_item_visible_in_cart` | Added item appears in cart |
| `test_cart_page_url_is_correct` | Cart loads correct URL `/cart.html` |
| `test_item_removed_from_cart_successfully` | Item removed from cart after clicking remove |
| `test_cart_badge_decrements_after_item_removal` | Cart badge disappears after removing only item |
| `test_continue_shopping_button_visible_in_cart` | Continue shopping button visible on cart page |

### Checkout
| Test | Description |
|------|-------------|
| `test_complete_checkout_flow` | E2E — add item → cart → checkout → confirm order |
| `test_checkout_missing_firstname` | Error shown when first name missing on checkout form |
| `test_checkout_missing_lastname` | Error shown when last name missing on checkout form |
| `test_checkout_missing_postalcode` | Error shown when postal code missing on checkout form |

---

## 🏗 POM Design
| File | Responsibility |
|---|---|
| `login_page.py` | Login |
| `product_page.py` | Add/remove items, cart badge |
| `cart_page.py` | View cart, remove, proceed to checkout |
| `checkout_page.py` | Fill details, submit, confirm order |
| `conftest.py` | Fixtures — login_page, logged_in_page, cart_page, checkout_page |

---

## ⚙️ Setup & Run

```bash
git clone https://github.com/dona126/playwright-pytest-suite.git
cd playwright-pytest-suite
pip install -r requirements.txt
python -m playwright install
```

---

## 🔐 Environment Variables
Create `.env` in root:
BASE_URL=https://www.saucedemo.com
SAUCE_PASSWORD=secret_sauce

---

### Local (VS Code)
```bash
# single browser
pytest --browser chromium --screenshot only-on-failure --html=report.html --self-contained-html

# multi browser parallel
pytest --browser chromium --browser firefox --browser webkit -n 3 --html=report.html --self-contained-html
```

---

## 🔁 CI/CD

[![Playwright Tests](https://github.com/dona126/playwright-pytest-suite/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/dona126/playwright-pytest-suite/actions/workflows/playwright-tests.yml)

- Runs in parallel across **Chromium, Firefox, WebKit**
- Screenshots + videos auto-captured on failure

---

### GitHub Secrets Required
`Repo → Settings → Secrets and variables → Actions`

| Secret Name | Description |
|---|---|
| `SAUCE_PASSWORD` | SauceDemo login password |
| `BASE_URL` | SauceDemo base URL |

---

## 📊 Test Reports

- HTML report + screenshots auto-generated on every CI run
- Download from: `Actions → your run → Artifacts`

| Artifact | Contents |
|---|---|
| `test-results-chromium` | report + screenshots |
| `test-results-firefox` | report + screenshots |
| `test-results-webkit` | report + screenshots |

---

## 🌐 Browsers Tested

| Browser | Local | CI |
|---|---|---|
| Chromium | ✅ | ✅ |
| Firefox | ✅ | ✅ |
| WebKit | ✅ | ✅ |

