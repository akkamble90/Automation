import pytest
import time
from security_automation.utils.payloads import WEAK_PASSWORDS
from security_automation.utils.logger import log_info
from security_automation.utils.helpers import take_screenshot
from security_automation.core.config import BASE_URL
from security_automation.pages.login import LoginPage

def test_weak_auth(driver):
    page = LoginPage(driver)
    page.open(f"{BASE_URL}/#/login")
    
    found = False
    for pwd in WEAK_PASSWORDS:
        log_info(f"Testing: {pwd}")
        page.login("admin@juice-sh.op", pwd)
        time.sleep(1.5) # Wait for login processing

        # Success check: URL change or Presence of 'Account' button
        if "/login" not in driver.current_url:
            log_info(f"VULNERABILITY FOUND: Password '{pwd}' works!")
            take_screenshot(driver, f"success_{pwd}")
            found = True
            break
        
        driver.get(f"{BASE_URL}/#/login")

    assert found, "No weak passwords worked."