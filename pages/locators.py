from selenium.webdriver.common.by import By


class HomePageLocators():
    LOGIN_LINK = (By.ID, "login2")
    LOGOUT_LINK = (By.ID, "logout2")
    SAMSUNG_GALAXY_S6 = (By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")
    WELCOME_USER = (By.ID, "nameofuser")


class LoginPageLocators():
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")


class GalaxyS6PageLocators():
    ADD_TO_CART = (By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
    GO_TO_CART = (By.ID, "cartur")


class CartPageLocators():
    PLACE_ORDER_BUTTON = (By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
    ITEM_NAME = (By.XPATH, "//*[@id='tbodyid']/tr/td[2]")
    DELETE_BUTTON = (By.XPATH, "//*[@id='tbodyid']/tr/td[4]/a")


class PlaceOrderPageLocators():
    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CREDIT_CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE_BUTTON = (By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
    OK_ORDER_PLACED_BUTTON = (By.XPATH, "/html/body/div[10]/div[7]/div/button")
