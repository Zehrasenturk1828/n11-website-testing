import pytest
from Pages.ProductDetails import *
import softest


@pytest.mark.usefixtures("setup")
class TestProductDetails(softest.TestCase):

    #TS-03 TC-01
    def test_product_detail_check(self):
        product_detail = Product_details_check(self.driver)

        product_detail.sendkeys_to_searchbox()
        product_detail.click_searchbutton()
        product_detail.click_a_product()
        product_detail.take_screenshot("screenshots/productdetails.png")
        product_detail.click_screensize_info()
        product_detail.click_more_features_button()

    #TS-03 TC-02
    def test_product_change_options(self):
        product_options = Changing_product_options(self.driver)

        product_options.sendkeys_to_searchbox()
        product_options.click_searchbutton()
        product_options.click_a_product()
        product_options.click_change_options_button()
        product_options.select_color()
        product_options.select_memory()
        product_options.change_product()
        self.soft_assert(self.assertEqual, "Beyaz, 256GB", product_options.verify_product_info(), "ERROR MESSAGE")

    #TS-03 TC-03
    def test_product_tabs_control(self):
        product_tabs = Checking_product_details_tabs(self.driver)

        product_tabs.sendkeys_to_searchbox()
        product_tabs.click_searchbutton()
        product_tabs.click_a_product()
        product_tabs.click_info_tab()
        self.soft_assert(self.assertEqual, "Ürün Detayları", product_tabs.verify_info_tab(), "ERROR MESSAGE")
        time.sleep(4)
        product_tabs.click_reviews_tab()
        self.soft_assert(self.assertEqual, "Ürün Değerlendirmeleri", product_tabs.verify_reviews_tab(), "ERROR MESSAGE")
        time.sleep(4)      
        product_tabs.click_sellers_tab()
        self.soft_assert(self.assertEqual, "Diğer Mağazalar", product_tabs.verify_sellers_tab(), "ERROR MESSAGE")
        time.sleep(4)
        product_tabs.click_shipment_tab()
        self.soft_assert(self.assertEqual, "Teslimat Bilgileri", product_tabs.verify_shipment_tab(), "ERROR MESSAGE")
        time.sleep(4)
        product_tabs.click_payment_tab()
        self.soft_assert(self.assertEqual, "Taksit Seçenekleri", product_tabs.verify_payment_tab(), "ERROR MESSAGE")
        time.sleep(4)