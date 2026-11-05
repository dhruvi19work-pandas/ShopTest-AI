
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from test_data.login_data import INVALID_LOGIN_DATA
import os

import pytest


@pytest.mark.ui
@pytest.mark.smoke
def test_login_page_loads(page):
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)

    login_page.open(base_url)

    assert login_page.username_input.is_visible()
    assert login_page.password_input.is_visible()
    assert login_page.login_button.is_visible()



@pytest.mark.ui
@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    INVALID_LOGIN_DATA,
    ids=["invalid-username", "invalid-password", "empty-username"],
)
def test_invalid_login(page, username, password, expected_error):

    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)

    login_page.open(base_url)

    login_page.login(username, password)

    error_message = login_page.get_error_message()

    assert expected_error in error_message



@pytest.mark.ui
def test_login_page_starts_fresh(page):
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    page.goto(base_url)

    assert page.locator("#user-name").input_value() == ""
    assert page.locator("#password").input_value() == ""


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(page):

    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.open(base_url)

    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)

    assert products_page.is_open()
    assert products_page.get_title() == "Products"



@pytest.mark.ui
@pytest.mark.smoke
def test_add_backpack_to_cart(page):

    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"



@pytest.mark.ui
@pytest.mark.regression
def test_remove_backpack_from_cart(page):

    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)

    products_page.add_backpack_to_cart()

    assert products_page.get_cart_count() == "1"

    products_page.remove_backpack_from_cart()

    assert products_page.cart_badge.is_hidden()