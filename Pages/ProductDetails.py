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

#TS-03 TC-01
class Product_details_check(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(2)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(2) 

    def click_a_product(self):
        self.wait_element_presence(PRODUCT_XPATH).click()

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def click_screensize_info(self):
        self.wait_element_visibility(SCREENSIZE_XPATH).click()

    def click_more_features_button(self):
        self.wait_element_visibility(MORE_FEATURES_XPATH).click()
        time.sleep(5)

#TS-03 TC-02
class Changing_product_options(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(2)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(2) 

    def click_a_product(self):
        self.wait_element_presence(PRODUCT_XPATH).click()

    def click_change_options_button(self):
        self.wait_element_presence(PRODUCT_INFO_XPATH).click()

    def select_color(self):
        self.wait_element_visibility(PRODUCT_COLOR_XPATH).click()

    def select_memory(self):
        self.wait_element_visibility(PRODUCT_MEMORY_XPATH).click()

    def change_product(self):
        self.wait_element_visibility(SELECT_PRODUCT_XPATH).click()

    def verify_product_info(self):
        product_info = self.wait_element_presence(PRODUCT_INFO_XPATH)
        return product_info.text
    
#TS-03 TC-03
class Checking_product_details_tabs(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys(PRODUCT_NAME)
        time.sleep(2)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(2) 

    def click_a_product(self):
        self.wait_element_presence(PRODUCT_XPATH).click()

    def click_info_tab(self):
        self.wait_element_presence(PD_INFO_XPATH).click()

    def verify_info_tab(self):
        product_info = self.wait_element_presence(INFO_TITLE_XPATH)
        return product_info.text
    
    def click_reviews_tab(self):
        self.wait_element_presence(PD_REVIEW_XPATH).click()

    def verify_reviews_tab(self):
        product_reviews = self.wait_element_presence(REVIEW_TITLE_XPATH)
        return product_reviews.text
    
    def click_sellers_tab(self):
        self.wait_element_presence(PD_SELLER_XPATH).click()

    def verify_sellers_tab(self):
        product_sellers = self.wait_element_presence(SELLER_TITLE_XPATH)
        return product_sellers.text
    
    def click_shipment_tab(self):
        self.wait_element_presence(PD_SHIPMENT_XPATH).click()

    def verify_shipment_tab(self):
        product_shipment = self.wait_element_presence(SHIPMENT_TITLE_XPATH)
        return product_shipment.text
    
    def click_payment_tab(self):
        self.wait_element_presence(PD_PAYMENT_XPATH).click()

    def verify_payment_tab(self):
        product_payment = self.wait_element_presence(PAYMENT_TITLE_XPATH)
        return product_payment.text
        

    
        