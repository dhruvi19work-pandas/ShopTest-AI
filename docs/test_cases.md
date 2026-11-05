# ShopTest-AI — Detailed Test Cases

**Application:** SauceDemo  
**URL:** https://www.saucedemo.com/  
**Browser:** Chromium  
**Test Framework:** Python + Playwright + Pytest

---

## TC-001: Login with Valid Credentials

**Priority:** High  
**Type:** Positive

**Preconditions:**
- Application is accessible.
- User is on the login page.

**Test Data:**
- Username: standard_user
- Password: secret_sauce

**Test Steps:**
1. Open SauceDemo.
2. Enter a valid username.
3. Enter a valid password.
4. Click the Login button.

**Expected Result:**
- User successfully logs in.
- Inventory page is displayed.
- Product listings are visible.

---

## TC-002: Login with Invalid Credentials

**Priority:** High  
**Type:** Negative

**Preconditions:**
- User is on the login page.

**Test Data:**
- Username: invalid_user
- Password: wrong_password

**Test Steps:**
1. Open SauceDemo.
2. Enter an invalid username.
3. Enter an invalid password.
4. Click Login.

**Expected Result:**
- Login is rejected.
- An appropriate error message is displayed.
- User remains on the login page.

---

## TC-003: Login with Empty Fields

**Priority:** High  
**Type:** Negative

**Preconditions:**
- User is on the login page.

**Test Steps:**
1. Open SauceDemo.
2. Leave username empty.
3. Leave password empty.
4. Click Login.

**Expected Result:**
- Login is rejected.
- A validation error is displayed.
- User does not enter the inventory page.

---

## TC-004: Verify Product Sorting by Price

**Priority:** Medium  
**Type:** Functional

**Preconditions:**
- User is successfully logged in.
- Inventory page is displayed.

**Test Steps:**
1. Locate the product sorting dropdown.
2. Select Price (low to high).
3. Observe the displayed product prices.

**Expected Result:**
- Products are arranged from lowest to highest price.
- All displayed products remain visible.

---

## TC-005: Add Product to Cart

**Priority:** High  
**Type:** Functional

**Preconditions:**
- User is logged in.
- Inventory page is displayed.

**Test Steps:**
1. Select a product.
2. Click its Add to Cart button.
3. Observe the shopping cart icon.

**Expected Result:**
- Selected product is added to the cart.
- Cart count updates correctly.
- Product appears in the shopping cart.

---

## TC-006: Remove Product from Cart

**Priority:** Medium  
**Type:** Functional

**Preconditions:**
- User is logged in.
- At least one product is added to the cart.

**Test Steps:**
1. Open the shopping cart.
2. Locate the selected product.
3. Click Remove.

**Expected Result:**
- Product is removed from the cart.
- Cart contents update correctly.

---

## TC-007: Checkout with Valid Information

**Priority:** High  
**Type:** Positive

**Preconditions:**
- User is logged in.
- At least one product is in the cart.

**Test Data:**
- First Name: Test
- Last Name: User
- Postal Code: 395001

**Test Steps:**
1. Open the cart.
2. Click Checkout.
3. Enter first name.
4. Enter last name.
5. Enter postal code.
6. Click Continue.

**Expected Result:**
- Checkout information is accepted.
- Order overview page is displayed.

---

## TC-008: Complete Purchase

**Priority:** High  
**Type:** End-to-End

**Preconditions:**
- User is logged in.
- At least one product is in the cart.
- Valid checkout information has been submitted.

**Test Steps:**
1. Review the order overview.
2. Verify product details and total amount.
3. Click Finish.

**Expected Result:**
- Order completion confirmation is displayed.
- Purchase workflow finishes successfully.

---

## TC-009: Logout Successfully

**Priority:** Medium  
**Type:** Functional

**Preconditions:**
- User is logged in.

**Test Steps:**
1. Open the navigation menu.
2. Click Logout.

**Expected Result:**
- User is redirected to the login page.
- Authenticated inventory access is no longer available.

---

## Test Execution Status

All nine workflows have been explored manually.

Automated execution: Pending.