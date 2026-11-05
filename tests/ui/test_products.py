import pytest

from pages.products_page import ProductsPage


@pytest.mark.ui
@pytest.mark.regression
def test_sort_products_by_price_low_to_high(logged_in_page):

    products_page = ProductsPage(logged_in_page)

    products_page.sort_products("lohi")

    prices = products_page.get_product_prices()

    assert prices == sorted(prices)



@pytest.mark.ui
@pytest.mark.regression
def test_cart_badge_appears_after_adding_product(logged_in_page):

    products_page = ProductsPage(logged_in_page)

    products_page.add_backpack_to_cart()

    products_page.wait_for_cart_badge()

    assert products_page.get_cart_count() == "1"



@pytest.mark.ui
@pytest.mark.regression
def test_add_different_product_to_cart(logged_in_page):

    products_page = ProductsPage(logged_in_page)

    products_page.add_product_to_cart("Sauce Labs Bike Light")

    products_page.wait_for_cart_badge()

    assert products_page.get_cart_count() == "1"

