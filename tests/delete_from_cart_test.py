from tests.base_test import BaseTest



class DeleteFromCartTest(BaseTest):
    """
    Test of item removal from cart
    """
    def test_delete_galaxy_s6_from_cart(self):
        """
        TC04 Testcase verifies removing from cart an item
        """
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.add_to_cart()
        self.galaxy_s6_page.confirm_adding_to_cart()
        # Test starts here, after preconditions are fulfilled
        self.cart_page.click_delete()
        no_items_in_cart = []
        # self.assertCountEqual(cart_page.get_galaxy_s6_in_cart(), no_items_in_cart)
