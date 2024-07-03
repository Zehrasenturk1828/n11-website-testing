import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.constants.GloabalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase
import pyautogui
import random
import string

@pytest.mark.usefixtures("setup")
class Selecting_subcategory(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def hover_over_category(self):
        aChains = ActionChains(self.driver)
        hover_on = self.wait_element_visibility(CATEGORY_XPATH)
        aChains.move_to_element(hover_on).perform()
        time.sleep(4)

    def click_subcategory(self):
        self.wait_element_visibility(SUBCATEGORY_XPATH).click()
        time.sleep(4) 

    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(RESULT_TEXT_CLASS)
        return products_list_result.text

class Selecting_maincategory(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver   

    def click_category(self):
        self.wait_element_visibility(CATEGORY_XPATH).click()
        time.sleep(4)
    
    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)


    def click_subcategory(self):
        self.wait_element_visibility(WOMENS_CLOTHING_XPATH).click()
        time.sleep(4)

    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(BREADCRUMB_XPATH)
        return products_list_result.text
    
class Selecting_brandcategory(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver   

    def click_category(self):
        self.wait_element_visibility(CATEGORY_XPATH).click()
        time.sleep(4)
    
    def click_brandcategory_mavi(self):
        self.wait_element_visibility(BRAND_MAVI_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(SELLER_NAME_XPATH)
        return products_list_result.text