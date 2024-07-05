import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Pages.constants.GloabalConstants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Pages.PageBase import PageBase

@pytest.mark.usefixtures("setup")
#TS-02 TC-01
class Add_product_to_product_cart(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys("Etek")
        time.sleep(2)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(2) 

    def click_a_product(self):
        self.wait_element_presence(SKIRT_XPATH).click()

    def click_add_to_basket(self):
        self.wait_element_presence(ADD_BASKET_BUTTON_XPATH).click()

    def click_basket(self):
        self.wait_element_presence(CLICK_BASKET_XPATH).click()

    def get_product_price(self):
        price_text = self.wait_element_presence(PRODUCT_PRICE).text
        price_text = price_text.replace('.', '').replace(',', '.').replace(' TL', '').replace('₺', '').strip()
        return float(price_text)

    def set_product_quantity(self, quantity):
        quantity_button = self.wait_element_presence(SPINNER_UP)
        for _ in range(quantity - 1):
            quantity_button.click()

    def discount_per_item(self):
        try:
            discount_price = self.wait_element_presence(DISCOUNT_PRICE).text
            if discount_price.strip():
                discount_price = discount_price.replace('.', '').replace(',', '.').replace(' TL', '').replace('₺', '').strip()
                return float(discount_price)
            else:
                return 0.0
        except NoSuchElementException:
            return 0.0

    def get_total_price(self):
        total_price_text = self.wait_element_presence(TOTAL_PRICE).text
        if total_price_text.strip():
            total_price_text = total_price_text.replace('.', '').replace(',', '.').replace(' TL', '').replace('₺', '').strip()
            return float(total_price_text)
        else:
            return 0.0 
#TS-02 TC-02       
class Remove_product_to_product_cart(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def sendkeys_to_searchbox(self):
        searchbox = self.wait_element_visibility(SEARCHBOX_XPATH)
        searchbox.send_keys("Etek")
        time.sleep(2)

    def click_searchbutton(self):
        self.wait_element_visibility(SEND_BUTTON).click()
        time.sleep(2) 

    def click_a_product(self):
        self.wait_element_presence(SKIRT_XPATH).click()

    def click_add_to_basket(self):
        self.wait_element_presence(ADD_BASKET_BUTTON_XPATH).click()

    def click_basket(self):
        self.wait_element_presence(CLICK_BASKET_XPATH).click()

    def click_remove_button(self):
        self.wait_element_presence(REMOVE_BUTTON).click()

    def confirm_delete(self):
        self.wait_element_presence(DELETE_BUTTON_ID).click()

    def verify_empty_basket(self):
        empty_basket = self.wait_element_presence(EMPTY_BASKET_MESSAGE)
        return empty_basket.text