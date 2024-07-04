import pytest
import pyautogui
from selenium import webdriver
from Pages.ProductFiltering import *
import softest


@pytest.mark.usefixtures("setup")
class TestProductFiltering(softest.TestCase):
    def test_Searchbutton_function_control(self):

        SearchButton_control = Searchbutton_function_control(self.driver)
        SearchButton_control.sendkeys_to_searchbox()
        SearchButton_control.click_searchbutton()
        self.soft_assert(self.assertEqual, PRODUCT_CATEGORY_PATH_TEXT, SearchButton_control.verify_listed_products(), "HATALI MESAJ")
        self.assert_all()


    def test_control_pricerange_filters(self):

        control_pricerange_filters = Control_Price_Range_filters(self.driver)
        control_pricerange_filters.sendkeys_to_searchbox()
        control_pricerange_filters.click_searchbutton()
        control_pricerange_filters.sendkeys_to_min()
        control_pricerange_filters.sendkeys_to_max()
        control_pricerange_filters.confirm_filters()
        self.soft_assert(self.assertEqual, FILTER_GROUP_TEXT, control_pricerange_filters.verify_listed_products(), "HATALI MESAJ")
        self.assert_all()
    
    def test_control_brand_filters(self):

        control_brand_filters = Control_Brand_filters(self.driver)
        control_brand_filters.sendkeys_to_searchbox()
        control_brand_filters.click_searchbutton()
        self.driver.execute_script("window.scrollTo(0, 250)")
        control_brand_filters.select_brand()
        self.soft_assert(self.assertEqual, BRAND_FILTER_GROUP_TEXT, control_brand_filters.verify_listed_products(), "HATALI MESAJ")
        self.assert_all()