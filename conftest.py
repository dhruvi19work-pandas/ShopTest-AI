import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


@pytest.fixture(scope="session")
def browser():
    browser_name = os.getenv("BROWSER", "chromium")

    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)

        browser = browser_type.launch(
            headless=os.getenv("HEADLESS", "true").lower() == "true"
        )

        yield browser

        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.set_default_timeout(
        int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    )

    yield page

    context.close()