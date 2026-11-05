import pytest

from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.ui
@pytest.mark.smoke
def test_complete_checkout(logged_in_page):

    products_page = ProductsPage(logged_in_page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    assert cart_page.is_open()
    assert cart_page.get_item_count() == 1

    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.fill_customer_information(
        "John",
        "Smith",
        "395007"
    )

    checkout_page.continue_to_overview()

    assert checkout_page.is_overview_open()

    checkout_page.finish_order()

    assert checkout_page.is_order_complete()
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"



@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        (
            "",
            "Smith",
            "395007",
            "Error: First Name is required"
        ),
        (
            "John",
            "",
            "395007",
            "Error: Last Name is required"
        ),
        (
            "John",
            "Smith",
            "",
            "Error: Postal Code is required"
        ),
    ]
)
def test_checkout_required_field_validation(
    logged_in_page,
    first_name,
    last_name,
    postal_code,
    expected_error
):

    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.fill_customer_information(
        first_name,
        last_name,
        postal_code
    )

    checkout_page.continue_to_overview()

    assert checkout_page.get_error_message() == expected_error