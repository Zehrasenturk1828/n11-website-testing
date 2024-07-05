import pytest
import pyautogui
from selenium import webdriver
from Pages.ChangeIteminCart import *
import softest


@pytest.mark.usefixtures("setup")
class TestChangeIteminCart(softest.TestCase):
    #TS-02 TC-01
    def test_change_quantity_of_product(self):
        quantity_of_item = Add_product_to_product_cart(self.driver)
        quantity_of_item.sendkeys_to_searchbox()
        quantity_of_item.click_searchbutton()
        quantity_of_item.click_a_product()
        self.driver.execute_script("window.scrollTo(0, 280)")
        quantity_of_item.click_add_to_basket()
        time.sleep(3)
        quantity_of_item.click_basket()
        time.sleep(3)
        initial_product_price = quantity_of_item.get_product_price()
        initial_total_price = quantity_of_item.get_total_price()
        self.driver.execute_script("window.scrollTo(0, 260)")
        quantity_of_item.set_product_quantity(2)
        time.sleep(3)
        discount_per_item = quantity_of_item.discount_per_item()
        time.sleep(3)
        updated_total_price = quantity_of_item.get_total_price()
        time.sleep(3)
        discount_per_item_value = quantity_of_item.discount_per_item()
        if discount_per_item_value != 0.0:
            expected_total_price = (initial_product_price - discount_per_item_value) * 2
        else:
            expected_total_price = initial_product_price * 2
        self.soft_assert(self.assertEqual, updated_total_price, expected_total_price, "Total price didn't update correctly")

    #TS-02 TC-02
    def test_verify_empty_basket(self):
        verify_basket = Remove_product_to_product_cart(self.driver)
        verify_basket.sendkeys_to_searchbox()
        verify_basket.click_searchbutton()
        verify_basket.click_a_product()
        self.driver.execute_script("window.scrollTo(0, 280)")
        verify_basket.click_add_to_basket()
        time.sleep(3)
        verify_basket.click_basket()
        time.sleep(3)
        verify_basket.click_remove_button()
        time.sleep(3)
        verify_basket.confirm_delete()
        time.sleep(3)
        self.soft_assert(self.assertEqual, "Sepetin Boş Görünüyor", verify_basket.verify_empty_basket(), "ERROR MESSAGE")