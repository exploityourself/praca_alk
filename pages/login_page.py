from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def input_username(self, username):
        username_field = self.driver.find_element(*LoginPageLocators.USERNAME)
        username_field.send_keys(username)

    def input_password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_btn.click()

    def _verify_page(self):
        pass
