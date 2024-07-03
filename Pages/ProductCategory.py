from time import sleep, time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Pages.constants.GloabalConstants import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase

@pytest.mark.usefixtures("setup")
class Selecting_subcategory(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def hover_over_category(self):
        aChains = ActionChains(self.driver)
        hover_on = self.wait_element_visibility(CATEGORY_XPATH)
        aChains.move_to_element(hover_on).perform()
        time.sleep(3)

    def click_subcategory(self):
        self.wait_element_visibility(SUBCATEGORY_XPATH).click()
        time.sleep(3) 

    def verify_listed_products(self):
        products_list_result = self.wait_element_presence(RESULT_TEXT_CLASS)
        return products_list_result.text
    
