# 🧪 Playwright PyTest Suite

Full E2E test suite for [SauceDemo](https://www.saucedemo.com) built with
Playwright, PyTest, and POM — with GitHub Actions CI/CD.

---

## 🛠 Tech Stack

- Python 3.12 · Playwright · PyTest · POM · GitHub Actions

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

## ⚙️ Setup & Run

```bash
git clone https://github.com/dona126/playwright-pytest-suite.git
cd playwright-pytest-suite
pip install -r requirements.txt
playwright install chromium
pytest --headed
```

---

## 🔁 CI/CD

![Playwright Tests](https://github.com/dona126/playwright-pytest-suite/actions/workflows/playwright-tests.yml/badge.svg)

---
