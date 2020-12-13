from selenium.webdriver.common.by import By


class MainPageLocator:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.fade.in:first-child strong')
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '.fade.in:last-child strong')
    ADD_MESSAGES = (By.ID, 'messages')
