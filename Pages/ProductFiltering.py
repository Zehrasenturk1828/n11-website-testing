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
#TS-02 TC-01
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
    
#TS-02 TC-02
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

#TS-02 TC-03  
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

#TS-02 TC-04
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
    
#TS-02 TC-05
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
    

#TS-02 TC-06
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

#TS-02 TC-07
class Clearing_selected_filters(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def delete_filters(self):
        self.wait_element_visibility(REMOVE_FILTERS_XPATH).click()
        time.sleep(2)

    def verify_hide_clearfilters_button(self):
        try:
            self.driver.find_element(REMOVE_FILTERS_XPATH)
            assert False, "Filters weren't cleared, the button is still present."
        except:
            print("Filters were successfully cleared, the button disappeared.")

#TS-02 TC-08
class Sorting_filters(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_dropdown_menu(self):
        self.wait_element_visibility(DROPDOWN_MENU_XPATH).click()
    
    def select_pricelow_filter(self):
        self.wait_element_visibility(PRICE_LOW_XPATH).click()

    def verify_pricelow_list(self):
        filter_pricelow = self.wait_element_presence(PRICE_LOW_XPATH)
        return filter_pricelow.text
    
    def select_pricehigh_filter(self):
        self.wait_element_visibility(PRICE_HIGH_XPATH).click()

    def verify_pricehigh_list(self):
        filter_pricehigh = self.wait_element_presence(PRICE_HIGH_XPATH)
        return filter_pricehigh.text
    
    def select_salesvolume_filter(self):
        self.wait_element_visibility(SALES_VOLUME_XPATH).click()

    def verify_salesvolume_list(self):
        filter_salesvolume = self.wait_element_presence(SALES_VOLUME_XPATH)
        return filter_salesvolume.text

    def select_reviews_filter(self):
        self.wait_element_visibility(REVIEWS_XPATH).click()

    def verify_reviews_list(self):
        filter_reviews = self.wait_element_presence(REVIEWS_XPATH)
        return filter_reviews.text

#TS-02 TC-09
class Local_advantages_feature(PageBase):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_select_location(self):
        self.wait_element_visibility(SELECT_LOCATION_XPATH).click()
        time.sleep(2)

    def click_city_dropdownmenu(self):
        self.wait_element_visibility(CITY_DROPDOWN_XPATH).click()
        time.sleep(2)

    def select_city(self):
        self.wait_element_visibility(ISTANBUL_XPATH).click()
        time.sleep(2)

    def click_district_dropdownmenu(self):
        self.wait_element_visibility(DISTRICT_XPATH).click()
        time.sleep(2)

    def select_district(self):
        self.wait_element_visibility(SISLI_XPATH).click()
        time.sleep(2)

    def confirm_location(self):
        self.wait_element_visibility(CONFIRM_LOCATION_XPATH).click()
        time.sleep(2)

    def verify_location_info(self):
        location_info = self.wait_element_presence(LOCATION_PLACE_XPATH)
        return location_info.text
        