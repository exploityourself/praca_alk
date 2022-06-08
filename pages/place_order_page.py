from pages.base_page import BasePage
from pages.locators import PlaceOrderPageLocators


class PlaceOrderPage(BasePage):

    def input_name(self, name):
        name_field = self.driver.find_element(*PlaceOrderPageLocators.NAME)
        name_field.send_keys(name)

    def input_country(self, country):
        country_field = self.driver.find_element(*PlaceOrderPageLocators.COUNTRY)
        country_field.send_keys(country)

    def input_city(self, city):
        city_field = self.driver.find_element(*PlaceOrderPageLocators.CITY)
        city_field.send_keys(city)

    def input_credit_card(self, credit_card):
        credit_card_field = self.driver.find_element(*PlaceOrderPageLocators.CREDIT_CARD)
        credit_card_field.send_keys(credit_card)

    def input_month(self, month):
        month_field = self.driver.find_element(*PlaceOrderPageLocators.MONTH)
        month_field.send_keys(month)

    def input_year(self, year):
        year_field = self.driver.find_element(*PlaceOrderPageLocators.YEAR)
        year_field.send_keys(year)

    def click_purchase_button(self):
        purchase_btn = self.driver.find_element(*PlaceOrderPageLocators.PURCHASE_BUTTON)
        purchase_btn.click()

    def click_ok_button(self):
        ok_btn = self.driver.find_element(*PlaceOrderPageLocators.OK_ORDER_PLACED_BUTTON)
        ok_btn.click()

    def _verify_page(self):
        pass
