import pytest
import pyautogui
from selenium import webdriver
from Pages.ProductFiltering import *
import softest


@pytest.mark.usefixtures("setup")
class TestProductFiltering(softest.TestCase):

    #TS-02 TC-01
    def test_Searchbutton_function_control(self):

        SearchButton_control = Searchbutton_function_control(self.driver)
        SearchButton_control.sendkeys_to_searchbox()
        SearchButton_control.click_searchbutton()
        self.soft_assert(self.assertEqual, PRODUCT_CATEGORY_PATH_TEXT, SearchButton_control.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()

    #TS-02 TC-02
    def test_control_pricerange_filters(self):

        control_pricerange_filters = Control_Price_Range_filters(self.driver)
        control_pricerange_filters.sendkeys_to_searchbox()
        control_pricerange_filters.click_searchbutton()
        control_pricerange_filters.sendkeys_to_min()
        control_pricerange_filters.sendkeys_to_max()
        control_pricerange_filters.confirm_filters()
        self.soft_assert(self.assertEqual, FILTER_GROUP_TEXT, control_pricerange_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()
    
    #TS-02 TC-03
    def test_control_brand_filters(self):

        control_brand_filters = Control_Brand_filters(self.driver)
        control_brand_filters.sendkeys_to_searchbox()
        control_brand_filters.click_searchbutton()
        self.driver.execute_script("window.scrollTo(0, 250)")
        control_brand_filters.select_brand()
        self.soft_assert(self.assertEqual, BRAND_FILTER_GROUP_TEXT, control_brand_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()

    #TS-02 TC-04
    def test_control_category_filters(self):

        control_category_filters = Control_Category_filters(self.driver)
        control_category_filters.sendkeys_to_searchbox()
        control_category_filters.click_searchbutton()
        control_category_filters.select_subcategory()
        self.soft_assert(self.assertEqual, CATEGORY_BREADCRUMB_TEXT, control_category_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()
    
    #TS-02 TC-05
    def test_control_pr_filters(self):
        control_pr_filters = Control_ProductRating_filters(self.driver)

        control_pr_filters.sendkeys_to_searchbox()
        control_pr_filters.click_searchbutton()
        time.sleep(4)
        control_pr_filters.select_product_rating()
        self.soft_assert(self.assertEqual, PR_FILTER_GROUP_TEXT, control_pr_filters.verify_listed_products(), "ERROR MESSAGE")
        self.assert_all()

    #TS-02 TC-06
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
    
    #TS-02 TC-07
    def test_clearing_selected_filters(self):
        control_multiple_filters = Control_combination_multiple_filters(self.driver)
        control_del_selected_filters = Clearing_selected_filters(self.driver)

        control_multiple_filters.sendkeys_to_searchbox()
        control_multiple_filters.click_searchbutton()
        control_multiple_filters.select_subcategory()
        control_multiple_filters.sendkeys_to_min()
        control_multiple_filters.sendkeys_to_max()
        control_multiple_filters.confirm_filters()
        control_multiple_filters.select_brand()
        
        control_del_selected_filters.delete_filters()
        control_del_selected_filters.verify_hide_clearfilters_button()

    #TS-02 TC-08
    def test_sorting_filters(self):
        control_sorting_filters = Sorting_filters(self.driver)
        control_multiple_filters = Control_combination_multiple_filters(self.driver)

        control_multiple_filters.sendkeys_to_searchbox()
        control_multiple_filters.click_searchbutton()

        control_sorting_filters.click_dropdown_menu()
        control_sorting_filters.select_pricelow_filter()
        self.soft_assert(self.assertEqual, "Artan Fiyat", control_sorting_filters.verify_pricelow_list, "ERROR MESSAGE")
        control_sorting_filters.click_dropdown_menu()
        control_sorting_filters.select_pricehigh_filter()
        self.soft_assert(self.assertEqual, "Azalan Fiyat", control_sorting_filters.verify_pricehigh_list, "ERROR MESSAGE")
        control_sorting_filters.click_dropdown_menu()
        control_sorting_filters.select_salesvolume_filter()
        self.soft_assert(self.assertEqual, "Satış miktarı", control_sorting_filters.verify_salesvolume_list, "ERROR MESSAGE")
        control_sorting_filters.click_dropdown_menu()
        control_sorting_filters.select_reviews_filter()
        self.soft_assert(self.assertEqual, "Yorum sayısı", control_sorting_filters.verify_reviews_list, "ERROR MESSAGE")

    #TS-02 TC-09
    def test_local_advantages_feature(self):
        control_multiple_filters = Control_combination_multiple_filters(self.driver)
        control_local_advantages = Local_advantages_feature(self.driver)

        control_multiple_filters.sendkeys_to_searchbox()
        control_multiple_filters.click_searchbutton()
        control_local_advantages.click_select_location()
        control_local_advantages.click_city_dropdownmenu()
        control_local_advantages.select_city()
        control_local_advantages.click_district_dropdownmenu()
        control_local_advantages.select_district()
        control_local_advantages.confirm_location()
        self.soft_assert(self.assertEqual, "Şişli/İstanbul", control_local_advantages.verify_location_info(), "ERROR MESSAGE")