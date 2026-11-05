class ProductsPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.page_title = page.locator(".title")
        self.inventory_list = page.locator(".inventory_list")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )

        self.backpack_remove_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )

        self.product_sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.product_prices = page.locator(".inventory_item_price")

        self.inventory_items = page.locator(".inventory_item")

    # Page checks
    def is_open(self):
        return self.inventory_list.is_visible()

    def get_title(self):
        return self.page_title.inner_text()

    # Product actions
    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def remove_backpack_from_cart(self):
        self.backpack_remove_button.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()

    def open_cart(self):
        self.shopping_cart_link.click()

    def sort_products(self, sorting_option):
        self.product_sort_dropdown.select_option(sorting_option)

    def get_product_prices(self):
        prices = self.product_prices.all_inner_texts()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    def wait_for_cart_badge(self):
       self.cart_badge.wait_for(state="visible")


    def add_product_to_cart(self, product_name):
       product = self.inventory_items.filter(
        has_text=product_name
    )
       product.get_by_role(
        "button",
        name="Add to cart"
    ).click()