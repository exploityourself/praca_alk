from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.galaxy_s6_page import GalaxyS6Page
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def click_login_link(self):
        login_link = self.driver.find_element(*HomePageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(self.driver)

    def click_logout_button(self):
        logout_link = self.driver.find_element(*HomePageLocators.LOGOUT_LINK)
        logout_link.click()

    def click_galaxy_s6(self):
        galaxy_s6_btn = self.driver.find_element(*HomePageLocators.SAMSUNG_GALAXY_S6)
        galaxy_s6_btn.click()
        return GalaxyS6Page(self.driver)

    def _verify_page(self):
        pass
