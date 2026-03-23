from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from security_automation.pages.base_page import BasePage
import time

class SearchPage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, ".mat-search_icon-search, mat-icon[mattooltip*='search']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "mat-search-bar input, input[placeholder='Search…']")

    def search(self, payload):
        # 1. Dismiss banner via JS
        self.driver.execute_script("document.querySelector('button[aria-label=\"Close Welcome Banner\"]')?.click();")
        
        # 2. Click Icon
        self.safe_click(self.SEARCH_ICON)
        time.sleep(0.5) 
        
        # 3. Safe Typing with JS Argument Passing
        try:
            self.safe_type(self.SEARCH_INPUT, payload)
        except Exception:
            # FIX: Use arguments[0] to prevent the payload from breaking the JS syntax
            selector = "input[placeholder='Search…']"
            js_code = """
                var input = document.querySelector(arguments[0]);
                if(input) {
                    input.value = arguments[1];
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                }
            """
            self.driver.execute_script(js_code, selector, payload)
        
        # 4. Submit
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)