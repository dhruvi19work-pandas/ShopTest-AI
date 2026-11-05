# ShopTest-AI — Test Strategy

## 1. Objective

Validate the functionality and reliability of the SauceDemo e-commerce application through manual and automated testing.

## 2. Testing Scope

### UI Testing
- Login and logout
- Product inventory
- Product sorting
- Shopping cart
- Checkout
- Order completion

### API Testing
- API endpoint validation
- HTTP status codes
- Response validation
- Negative API scenarios

## 3. Test Suites

### Smoke Suite
Validates critical application functionality:
- Successful login
- Inventory page loading
- Add product to cart
- Checkout availability

### Regression Suite
Validates broader functionality:
- Login and logout
- Invalid login
- Product sorting
- Cart operations
- Checkout validation
- Purchase completion

### Negative Suite
Validates error handling:
- Invalid credentials
- Empty login fields
- Missing checkout information

## 4. Test Execution Approach

- Execute smoke tests after major changes.
- Execute regression tests before release.
- Execute negative tests to validate error handling.
- Capture screenshots and reports for failures.

## 5. Automation Tools

- Python
- Playwright
- Pytest
- Requests
- pytest-html

## 6. Reporting

Test execution results will be documented using automated HTML reports.

## 7. Current Status

Test strategy defined. Automation implementation pending.