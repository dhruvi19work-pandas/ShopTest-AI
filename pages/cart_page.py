class CartPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.page_title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator('[data-test="checkout"]')

    # Page checks
    def is_open(self):
        return self.page_title.inner_text() == "Your Cart"

    def get_item_count(self):
        return self.cart_items.count()

    def get_item_name(self):
        return self.item_names.first.inner_text()

    # Cart actions
    def click_checkout(self):
        self.checkout_button.click()