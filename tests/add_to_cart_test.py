from tests.base_test import BaseTest


class AddToCartTest(BaseTest):

    def add_galaxy_s6_to_cart(self):
        """
        TC03 Testcase verifies adding to cart an item
        """
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.click_add_to_cart()
        self.galaxy_s6_page.confirm_adding_to_cart()
        no_items_in_cart = []
        self.assertCountEqual(cart_page.get_galaxy_s6_in_cart(), no_items_in_cart)
