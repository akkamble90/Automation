from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(headless=False, use_zap=True):
    chrome_options = Options()
    
    if use_zap:
        # ZAP usually runs on localhost:8080
        ZAP_PROXY = "127.0.0.1:8080"
        chrome_options.add_argument(f'--proxy-server={ZAP_PROXY}')
        # Ignore SSL certificate errors (ZAP uses its own certs)
        chrome_options.add_argument('--ignore-certificate-errors')

    if headless:
        chrome_options.add_argument("--headless=new")
        
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver