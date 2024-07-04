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

    def click_searchbutton(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(SEND_BUTTON)).click()
        

    def select_brand(self):
        self.wait_element_visibility(BRAND_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(FILTER_GROUP_XPATH)
        return products_list_result.text


class Control_Category_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(CATEGORY_PRODUCT_NAME)
        

    def click_searchbutton(self):
        self.wait_element_presence(SEND_BUTTON).click()
        

    def select_subcategory(self):
        self.wait_element_visibility(CATEGORY_FILTER_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(BREADCRUMB_XPATH)
        return products_list_result.text
    

class Control_ProductRating_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(CATEGORY_PRODUCT_NAME)
        

    def click_searchbutton(self):
        self.wait_element_presence(SEND_BUTTON).click()
        

    def select_product_rating(self):
        self.driver.execute_script("window.scrollTo(0, 350)")
        self.wait_element_visibility(PRODUCT_RATING_FILTER_XPATH).click()
        time.sleep(4)
    
    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(FILTER_GROUP_XPATH)
        return products_list_result.text
    


class Control_combination_multiple_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    
    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(CATEGORY_PRODUCT_NAME)
        

    def click_searchbutton(self):
        self.wait_element_presence(SEND_BUTTON).click()

    def sendkeys_to_min(self):
        price_range_min = self.wait_element_visibility(PRICE_RANGE_MIN_XPATH)
        price_range_min.send_keys("100")
        time.sleep(4) 
    
    def sendkeys_to_max(self):
        price_range_max = self.wait_element_visibility(PRICE_RANGE_MAX_XPATH)
        price_range_max.send_keys("500")
        time.sleep(4) 
    
    def confirm_filters(self):
        self.wait_element_visibility(CONFIRM_FILTERS_XPATH).click()
        time.sleep(4)

    
    def select_subcategory(self):
        self.wait_element_visibility(MF_SUBCATEGORY_XPATH).click()
        time.sleep(4)

    def select_brand(self):
        self.wait_element_visibility(DEFACTO_BRAND_XPATH).click()
        time.sleep(4)

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)


class Clearing_selected_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    
        