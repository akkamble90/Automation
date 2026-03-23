import pytest
import os
from security_automation.core.driver_manager import get_driver
from security_automation.utils.helpers import take_screenshot

@pytest.fixture
def driver():
    # Toggle headless=True for background runs
    driver = get_driver(headless=False)
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