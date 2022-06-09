from tests.base_test import BaseTest
from time import sleep


class AddToCartTest(BaseTest):

    def test_add_galaxy_s6_to_cart(self):
        """
        TC03 Testcase verifies adding an item to cart
        """
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.add_to_cart()
        sleep(2)
        self.galaxy_s6_page.confirm_adding_to_cart()
        self.galaxy_s6_page.go_to_cart()
        self.assertEqual(self.cart_page.check_item_in_cart(), "Samsung galaxy s6")
