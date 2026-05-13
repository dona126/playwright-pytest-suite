# 🧪 Playwright PyTest Suite

Full E2E test suite for [SauceDemo](https://www.saucedemo.com) built with
Playwright, PyTest, and POM — with GitHub Actions CI/CD.

---

## 🛠 Tech Stack

- Python 3.12 · Playwright · PyTest · POM · GitHub Actions

---

## ✅ Test Coverage

| Module | Tests |
|--------|-------|
| Login | Valid, invalid, locked user, empty fields |
| Products | Count, add to cart, badge |
| Cart | Item in cart, remove, badge count |
| Checkout | Full E2E flow, validation |

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
