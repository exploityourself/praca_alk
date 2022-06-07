from pages.base_page import BasePage


class GalaxyS6Page(BasePage):
    def click_add_to_cart(self):
        pass

    def confirm_adding_to_cart(self):
        self.driver.switchTo().alert().accept()

    def _verify_page(self):
        pass
