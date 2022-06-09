from tests.base_test import BaseTest
from time import sleep


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
        sleep(2)
        self.galaxy_s6_page.confirm_adding_to_cart()
        self.galaxy_s6_page.go_to_cart()
        # Test starts here, after preconditions are fulfilled
        self.cart_page.click_delete()
        sleep(2)
        self.cart_page.check_item_in_cart()

