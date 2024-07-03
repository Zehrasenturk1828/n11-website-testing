import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    BASE_URL = "https://www.n11.com/"
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()