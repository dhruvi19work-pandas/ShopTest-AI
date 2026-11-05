# ShopTest-AI — Positive, Negative & Edge Cases

## 1. Positive Test Scenarios

| ID | Scenario | Expected Result |
|---|---|---|
| POS-001 | Login with valid credentials | Login successful |
| POS-002 | Add one product to cart | Cart count becomes 1 |
| POS-003 | Add multiple products | Cart count updates correctly |
| POS-004 | Sort products by price | Products sorted correctly |
| POS-005 | Complete checkout with valid data | Order confirmation displayed |

## 2. Negative Test Scenarios

| ID | Scenario | Expected Result |
|---|---|---|
| NEG-001 | Login with invalid username | Error displayed |
| NEG-002 | Login with invalid password | Error displayed |
| NEG-003 | Login with empty fields | Validation error displayed |
| NEG-004 | Checkout without first name | Validation error displayed |
| NEG-005 | Checkout without last name | Validation error displayed |
| NEG-006 | Checkout without postal code | Validation error displayed |

## 3. Edge Test Scenarios

| ID | Scenario | Expected Result |
|---|---|---|
| EDGE-001 | Add all available products to cart | All products added correctly |
| EDGE-002 | Remove every product from cart | Cart becomes empty |
| EDGE-003 | Sort products high to low | Descending price order |
| EDGE-004 | Navigate back from checkout | Previous checkout stage remains accessible |
| EDGE-005 | Refresh inventory page after login | Application handles refresh correctly |
| EDGE-006 | Attempt checkout with an empty cart | Checkout should not proceed with an order |

## 4. Test Coverage Notes

- Positive testing validates expected user workflows.
- Negative testing validates error handling.
- Edge testing validates unusual and boundary conditions.

## Execution Status

Scenario identification completed.

Automation implementation: Pending.