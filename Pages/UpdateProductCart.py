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
#TS-01 TC-01
class Add_product_to_product_cart(PageBase):
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

    def click_add_to_basket(self):
        self.wait_element_presence(ADD_BASKET_BUTTON_XPATH).click()

    def check_popup_message(self):
        popup_message = self.wait_element_presence(POP_UP_XPATH)
        return popup_message.text
    
    def click_basket(self):
        self.wait_element_presence(BASKET_XPATH).click()

    def check_basket(self):
        product_name = self.wait_element_presence(PROD_INFO_IN_BASKET_XPATH)
        return product_name.text
        
    