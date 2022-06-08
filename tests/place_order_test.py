from tests.base_test import BaseTest


class PlaceOrderTest(BaseTest):

    def test_place_order_without_name(self):
        """
        TC01 Tests verify successful purchase of an item
        """
        self.home_page.click_galaxy_s6()
        self.galaxy_s6_page.add_to_cart()
        self.galaxy_s6_page.confirm_adding_to_cart()
        self.cart_page.click_place_order()
        self.place_order_page.input_name()
        self.place_order_page.input_country()
        self.place_order_page.input_city()
        self.place_order_page.input_credit_card()
        self.place_order_page.input_month()
        self.place_order_page.input_year()
        self.place_order_page.click_place_order_button()
        # Order confirmation window is shown when purchase button is pressed after correct details are entered
        # It consists Ok button which can be used for verification of successful purchase operation.
        self.place_order_page.click_ok_button()
