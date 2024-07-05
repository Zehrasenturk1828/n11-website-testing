import pytest
import pyautogui
from selenium import webdriver
from Pages.ProductCategory import *
import softest


@pytest.mark.usefixtures("setup")
class TestProductCategory(softest.TestCase):

    #TS-01 TC-01
    def test_selecting_subcategory(self):

        Select_category = Selecting_subcategory(self.driver)
        Select_category.hover_over_category()
        Select_category.click_subcategory()
        self.soft_assert(self.assertEqual, RESULT_TEXT, Select_category.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()
    
    #TS-01 TC-02
    def test_selecting_maincategory(self):

        Select_maincategory = Selecting_maincategory(self.driver)
        Select_maincategory.click_category()
        self.driver.execute_script("window.scrollTo(0, 200)")
        Select_maincategory.take_screenshot("screenshots/maincategories.png")
        Select_maincategory.click_subcategory()
        self.soft_assert(self.assertEqual, BREADCRUMB_TEXT, Select_maincategory.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()

    #TS-01 TC-03
    def test_selecting_brandcategory(self):

        Select_brandcategory = Selecting_brandcategory(self.driver)
        Select_brandcategory.click_category()
        Select_brandcategory.click_brandcategory_mavi()
        self.soft_assert(self.assertEqual, BRAND_MAVI_TEXT, Select_brandcategory.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()