from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#from pages.constants.globalConstants import *


def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.driver.maximize_window()
    BASE_URL = "https://www.n11.com/"
    self.driver.get(BASE_URL)
  
def teardown_method(self, method):
    self.driver.quit()

    
