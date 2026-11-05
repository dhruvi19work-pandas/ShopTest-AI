# ShopTest-AI — Test Scenarios

## Application Under Test
SauceDemo — https://www.saucedemo.com/

## Test Environment
- Browser: Chromium
- Automation: Python + Playwright
- Test runner: Pytest

## Test Scenario Matrix

| Scenario ID | Test Scenario | Priority |
|---|---|---|
| TS-001 | Verify login with valid credentials | High |
| TS-002 | Verify login with invalid credentials | High |
| TS-003 | Verify login with empty fields | High |
| TS-004 | Verify successful navigation to inventory page | High |
| TS-005 | Verify product names and prices are displayed | High |
| TS-006 | Verify sorting products by name | Medium |
| TS-007 | Verify sorting products by price | Medium |
| TS-008 | Verify adding a product to cart | High |
| TS-009 | Verify removing a product from cart | Medium |
| TS-010 | Verify cart contents | High |
| TS-011 | Verify checkout information submission | High |
| TS-012 | Verify checkout with missing information | High |
| TS-013 | Verify order completion | High |
| TS-014 | Verify successful logout | Medium |

## Initial Manual Testing Observations

- Valid login: Successful
- Product inventory: Loaded successfully
- Product sorting: Worked successfully
- Add to cart: Successful
- Remove from cart: Successful
- Checkout information: Accepted
- Order completion: Successful
- Logout: Successful

## Test Status

Initial manual exploration completed.

Automated test implementation: Pending.