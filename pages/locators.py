from selenium.webdriver.common.by import By


class HomePageLocators():
    LOGIN_LINK = (By.ID, "login2")
    LOGOUT_LINK = (By.ID, "logout2")
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")


class LoginPageLocators():
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn btn-primary")

class GalaxyS6PageLocators():
    ADD_TO_CART = (By.CLASS_NAME, "btn btn-primary")
    GO_TO_CART = (By.ID, "cartur")


class CartPageLocators():
    PLACE_ORDER_BUTTON = (By.CLASS_NAME, "btn btn-success")
    ITEM_NAME = (By.XPATH, "//*[@id='tbodyid']/tr/td[2]")
    DELETE_BUTTON = (By.XPATH, "//*[@id='tbodyid']/tr/td[4]/a")


class PlaceOrderPageLocators():
    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "countruy")
    CITY = (By.ID, "city")
    CREDIT_CARD = (By.ID, "credit_card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
    OK_ORDER_PLACED_BUTTON = (By.CLASS_NAME, "confirm btn btn-lg btn-primary")