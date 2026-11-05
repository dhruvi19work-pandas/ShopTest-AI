# ShopTest-AI — Risk-Based Test Prioritization

## Risk Assessment Approach

Risk is evaluated using:

- Business Impact
- Likelihood of Failure

Priority is assigned based on the potential effect of a failure on the application and its users.

## Test Priority Matrix

| Test ID | Test Scenario | Business Impact | Priority |
|---|---|---|---|
| TC-001 | Valid login | Critical | P0 |
| TC-002 | Invalid login | High | P1 |
| TC-003 | Empty login fields | High | P1 |
| TC-004 | Product sorting | Medium | P2 |
| TC-005 | Add product to cart | High | P1 |
| TC-006 | Remove product from cart | Medium | P2 |
| TC-007 | Checkout information | Critical | P0 |
| TC-008 | Complete purchase | Critical | P0 |
| TC-009 | Logout | Medium | P2 |

## Execution Strategy

### P0 — Critical
Execute first. These tests validate essential application access and purchase functionality.

### P1 — High
Execute after critical smoke tests. These validate important business and error-handling workflows.

### P2 — Medium
Execute during the broader regression suite.

### P3 — Low
Execute when time and test coverage permit.

## Risk-Based Testing Benefits

- Focuses testing on high-impact functionality.
- Helps identify critical failures early.
- Improves regression test efficiency.
- Supports better release decisions.

## Status

Initial risk assessment completed.
Priorities are provisional and may change based on observed application behavior and business requirements.
