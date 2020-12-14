from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.LINK_TEXT, 'View basket')  # Подумать как лучше


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.fade.in:first-child strong')
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '.fade.in:last-child strong')
    SUCCESS_MESSAGES = (By.ID, 'messages')  # Убрать и заменить в тестах (Плохой локатор)


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
