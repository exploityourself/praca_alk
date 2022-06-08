from pages.base_page import BasePage
from pages.locators import CartPageLocators
from pages.place_order_page import PlaceOrderPage

class CartPage(BasePage):
    def click_delete(self):
        delete_btn = self.driver.find_element(*CartPageLocators.DELETE_BUTTON)
        delete_btn.click()

    def click_place_order(self):
        place_order_btn = self.driver.find_element(*CartPageLocators.PLACE_ORDER_BUTTON)
        place_order_btn.click()
        return PlaceOrderPage(self.driver)

    def get_galaxy_s6_in_cart(self):
        pass

    def _verify_page(self):
        pass
