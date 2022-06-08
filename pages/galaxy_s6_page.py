from pages.base_page import BasePage
from pages.locators import GalaxyS6PageLocators
from pages.cart_page import CartPage


class GalaxyS6Page(BasePage):
    def add_to_cart(self):
        add_btn = self.driver.find_element(*GalaxyS6PageLocators.ADD_TO_CART)
        add_btn.click()
    def confirm_adding_to_cart(self):
        # Confirm adding to cart by clicking OK on popup window
        self.driver.switchTo().alert().accept()
    def go_to_cart(self):
        cart_btn = self.driver.find_element(*GalaxyS6PageLocators.GO_TO_CART)
        cart_btn.click()
        return CartPage(self.driver)


    def _verify_page(self):
        pass
