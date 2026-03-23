import pytest
from security_automation.utils.payloads import XSS_PAYLOADS
from security_automation.utils.logger import log_info
from security_automation.utils.helpers import take_screenshot
from security_automation.core.config import BASE_URL
from security_automation.pages.search_page import SearchPage
from selenium.common.exceptions import UnexpectedAlertPresentException

def test_xss_detection(driver):
    page = SearchPage(driver)
    page.open(BASE_URL)
    
    vulnerable = False
    for payload in XSS_PAYLOADS:
        log_info(f"Testing XSS Payload: {payload}")
        try:
            page.search(payload)
            if payload in driver.page_source:
                log_info(f"VULNERABILITY: Payload reflected!")
                vulnerable = True
        except UnexpectedAlertPresentException:
            log_info("VULNERABILITY: Alert triggered!")
            driver.switch_to.alert.accept()
            vulnerable = True
        
        driver.get(BASE_URL) # Reset for next payload

    assert not vulnerable, "XSS Vulnerabilities detected!"