import pytest
from Pages.UpdateProductCart import *
import softest


@pytest.mark.usefixtures("setup")
#TS-01 TC-01
class TestProductCart(softest.TestCase):
    def test_add_product_to_basket(self):
        product_cart = Add_product_to_product_cart(self.driver)

        product_cart.sendkeys_to_searchbox()
        product_cart.click_searchbutton()
        product_cart.click_a_product()
        time.sleep(2)
        product_cart.click_add_to_basket()
        time.sleep(2)
        self.soft_assert(self.assertEqual, "Ürün sepetinize eklendi", product_cart.check_popup_message(), "ERROR MESSAGE")
        time.sleep(2)
        product_cart.click_basket()
        product_cart.check_basket()