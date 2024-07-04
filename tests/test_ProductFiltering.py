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
        self.soft_assert(self.assertEqual, PRODUCT_CATEGORY_PATH_TEXT, SearchButton_control.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()


    def test_control_pricerange_filters(self):

        control_pricerange_filters = Control_Price_Range_filters(self.driver)
        control_pricerange_filters.sendkeys_to_searchbox()
        control_pricerange_filters.click_searchbutton()
        control_pricerange_filters.sendkeys_to_min()
        control_pricerange_filters.sendkeys_to_max()
        control_pricerange_filters.confirm_filters()
        self.soft_assert(self.assertEqual, FILTER_GROUP_TEXT, control_pricerange_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()
    
    def test_control_brand_filters(self):

        control_brand_filters = Control_Brand_filters(self.driver)
        control_brand_filters.sendkeys_to_searchbox()
        control_brand_filters.click_searchbutton()
        self.driver.execute_script("window.scrollTo(0, 250)")
        control_brand_filters.select_brand()
        self.soft_assert(self.assertEqual, BRAND_FILTER_GROUP_TEXT, control_brand_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()


    def test_control_category_filters(self):

        control_category_filters = Control_Category_filters(self.driver)
        control_category_filters.sendkeys_to_searchbox()
        control_category_filters.click_searchbutton()
        control_category_filters.select_subcategory()
        self.soft_assert(self.assertEqual, CATEGORY_BREADCRUMB_TEXT, control_category_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()
    
    def test_control_pr_filters(self):

        control_pr_filters = Control_ProductRating_filters(self.driver)
        control_pr_filters.sendkeys_to_searchbox()
        control_pr_filters.click_searchbutton()
        time.sleep(4)
        control_pr_filters.select_product_rating()
        self.soft_assert(self.assertEqual, PR_FILTER_GROUP_TEXT, control_pr_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()

    def test_control_multiple_filters(self):
        control_multiple_filters = Control_combination_multiple_filters(self.driver)
        control_multiple_filters.sendkeys_to_searchbox()
        control_multiple_filters.click_searchbutton()
        control_multiple_filters.select_subcategory()
        control_multiple_filters.sendkeys_to_min()
        control_multiple_filters.sendkeys_to_max()
        control_multiple_filters.confirm_filters()
        control_multiple_filters.select_brand()
        control_multiple_filters.take_screenshot("screenshots\multiplefilters.png")