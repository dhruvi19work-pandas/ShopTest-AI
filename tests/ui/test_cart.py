import pytest

from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.ui
@pytest.mark.regression
def test_cart_displays_added_product(logged_in_page):

    products_page = ProductsPage(logged_in_page)

    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(logged_in_page)

    assert cart_page.is_open()
    assert cart_page.get_item_count() == 1
    assert cart_page.get_item_name() == "Sauce Labs Backpack"