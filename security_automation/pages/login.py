from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from security_automation.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginButton")

    def login(self, email, password):
        # Force-close banners that block the UI
        self.driver.execute_script("document.querySelector('button[aria-label=\"Close Welcome Banner\"]')?.click();")
        
        self.safe_type(self.EMAIL, email)
        self.safe_type(self.PASSWORD, password)
        
        # Press Enter on the password field instead of clicking the button
        pwd_field = self.driver.find_element(*self.PASSWORD)
        pwd_field.send_keys(Keys.ENTER)