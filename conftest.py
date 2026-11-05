from utils.logger import get_logger
from pages.login_page import LoginPage


import os

import pytest

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


logger = get_logger(__name__) 


load_dotenv()


@pytest.fixture(scope="session")
def browser():
    browser_name = os.getenv("BROWSER", "chromium")

    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)

        browser = browser_type.launch(
    headless=os.getenv("HEADLESS", "true").lower() == "true",
    slow_mo=1000
)

        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def page(browser, request):

    context = browser.new_context()
    page = context.new_page()

    page.set_default_timeout(
        int(os.getenv("DEFAULT_TIMEOUT", "10000"))
    )

    try:
        yield page

    finally:

        try:
            if (
                hasattr(request.node, "rep_call")
                and request.node.rep_call.failed
            ):

                os.makedirs(
                    "reports/screenshots",
                    exist_ok=True
                )

                screenshot_name = (
                    request.node.name.replace("/", "_")
                    .replace(" ", "_")
                )

                screenshot_path = (
                    f"reports/screenshots/{screenshot_name}.png"
                )

                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )

                print(
                    f"\nScreenshot saved: {screenshot_path}"
                )

        finally:
            context.close()



@pytest.fixture
def logged_in_page(page):

    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com")

    login_page = LoginPage(page)
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    if report.when == "call":

        if report.passed:
            logger.info("TEST PASSED: %s", item.nodeid)

        elif report.failed:
            logger.error("TEST FAILED: %s", item.nodeid)