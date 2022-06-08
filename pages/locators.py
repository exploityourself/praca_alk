from selenium.webdriver.common.by import By


class HomePageLocators():
    LOGIN_LINK = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CLASS, "btn btn-primary")
    LOGOUT_LINK = (By.ID, "logout2")
    WELCOME_USERNAME = (By.ID, "nameofuser")
    SAMSUNG_GALAXY_S6 = (By.LINKTEXT, "Samsung galaxy s6")


class GalaxyS6PageLocators():
    ADD_TO_CART = (By.CLASS, "btn btn-primary")


class CartPageLocators():
    PLACE_ORDER_BUTTON = (By.CLASS, "btn btn-success")
    ITEM_NAME = (By.XPATH, "//*[@id='tbodyid']/tr/td[2]")
    DELETE_BUTTON = (By.XPATH, "//*[@id='tbodyid']/tr/td[4]/a")
