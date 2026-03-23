import pytest
import os
from security_automation.core.driver_manager import get_driver
from security_automation.utils.helpers import take_screenshot

@pytest.fixture(scope="function")
def driver():
    # GitHub sets the 'CI' environment variable to 'true' by default.
    is_github_actions = os.getenv('CI', 'false').lower() == 'true'
    # If on GitHub, use headless=True. If on your laptop, use headless=False to see the browser.
    driver = get_driver(headless=is_github_actions)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            take_screenshot(driver, f"FAIL_{item.name}")
