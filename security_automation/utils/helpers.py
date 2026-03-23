import os
import re
from datetime import datetime

def take_screenshot(driver, name="error"):
    os.makedirs("reports/screenshots", exist_ok=True)
    # Sanitize the name to remove illegal filename characters like <, >, :, ", /, \, |, ?, *
    clean_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    file_name = f"reports/screenshots/{clean_name}_{datetime.now().strftime('%H%M%S')}.png"
    driver.save_screenshot(file_name)
    return file_name