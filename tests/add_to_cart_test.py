from tests.base_test import BaseTest


class AddToCartTest(BaseTest):
    def add_galaxy_s6_to_cart(self):
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.click_add_to_cart()
        self.galaxy_s6_page.confirm_adding_to_cart()
        self.cart_page.verify_galaxy_s6_in_cart()
