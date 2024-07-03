import pytest
import pyautogui
from selenium import webdriver
from Pages.ProductCategory import *
import softest

@pytest.mark.usefixtures("setup")
class TestProductCategory:
    def test_selecting_subcategory(self):

        Select_category = Selecting_subcategory(self.driver)
        Select_category.hover_over_category()
        Select_category.click_subcategory()
        self.soft_assert(self.assertEqual, RESULT_TEXT, Select_category.verify_listed_products(), "HATALI MESAJ")
        self.assert_all()
