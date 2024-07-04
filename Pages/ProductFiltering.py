import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.constants.GloabalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase

@pytest.mark.usefixtures("setup")
class Searchbutton_function_control(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(4)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(4) 

    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(PRODUCT_CATEGORY_PATH)
        return products_list_result.text

class Control_Price_Range_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(4)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(4)

    def sendkeys_to_min(self):
        price_range_min = self.wait_element_visibility(PRICE_RANGE_MIN_XPATH)
        price_range_min.send_keys(PRICE_RANGE_MIN)
        time.sleep(4) 
    
    def sendkeys_to_max(self):
        price_range_max = self.wait_element_visibility(PRICE_RANGE_MAX_XPATH)
        price_range_max.send_keys(PRICE_RANGE_MAX)
        time.sleep(4) 
    
    def confirm_filters(self):
        self.wait_element_visibility(CONFIRM_FILTERS_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(FILTER_GROUP_XPATH)
        return products_list_result.text
    
class Control_Brand_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(4)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(4)

    def select_brand(self):
        self.wait_element_visibility(BRAND_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(FILTER_GROUP_XPATH)
        return products_list_result.text
