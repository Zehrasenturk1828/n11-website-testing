import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options() 
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
    chrome_options.add_argument("--disable-extensions") 
    chrome_options.add_argument("--disable-plugins-discovery") 
    chrome_options.add_argument("--disable-popup-blocking") 
    chrome_options.add_argument("--disable-save-password-bubble") 
    chrome_options.add_argument("--disable-translate") 
    chrome_options.add_argument("--disable-notifications") 
    chrome_options.add_argument("--disable-default-apps") 
    chrome_options.add_argument("--disable-infobars") 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    BASE_URL = "https://www.n11.com/"
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()