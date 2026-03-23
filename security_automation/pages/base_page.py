from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from security_automation.core.config import TIMEOUT
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def safe_click(self, locator):
        """Attempts a standard click; falls back to JS if intercepted."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def safe_type(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.click()
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(text)
        except Exception:
            element = self.driver.find_element(*locator)
            # FIX: Pass 'text' as an argument instead of using f-strings
            self.driver.execute_script("arguments[0].value = arguments[1];", element, text)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", element)