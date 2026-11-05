class CheckoutPage:

    def __init__(self, page):
        self.page = page

        # Customer information locators
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')

        # Checkout overview locators
        self.summary_info = page.locator(".summary_info")
        self.finish_button = page.locator('[data-test="finish"]')

        # Order confirmation locator
        self.complete_header = page.locator(".complete-header")

        self.error_message = page.locator('[data-test="error"]')

    # Checkout actions
    def fill_customer_information(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    # Page checks
    def is_overview_open(self):
        return self.summary_info.is_visible()

    def is_order_complete(self):
        return self.complete_header.is_visible()

    def get_confirmation_message(self):
        return self.complete_header.inner_text()

    def get_error_message(self):
        return self.error_message.inner_text()