
class LoginPage:

    def __init__(self, page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    # Page actions
    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()

    def is_login_successful(self):
        return self.page.locator(".inventory_list").is_visible()
