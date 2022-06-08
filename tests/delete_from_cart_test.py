from tests.base_test import BaseTest


class DeleteFromCartTest(BaseTest):
    def delete_galaxy_s6_from_cart(self):
        """
        TC04 Testcase verifies removing from cart an item
        """
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.click_add_to_cart()
        self.galaxy_s6_page.confirm_adding_to_cart()
        self.cart_page.click_delete()
        no_items_in_cart = []
        self.assertCountEqual(cart_page.get_galaxy_s6_in_cart(), no_items_in_cart)
