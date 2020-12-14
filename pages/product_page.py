from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super(ProductPage, self).__init__(browser, url)
        self.product_name = None
        self.product_price = None

    def add_product_to_basket(self):
        # Добавление товара в корзину
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_add_button(self):
        # Проверка наличия кнопки просмотра корзины на странице
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Add button not found'

    def product_names_should_match(self):
        # Проверка на совпадение имен добавленного товара, с тем, который есть в корзине
        name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert self.product_name == name, 'The names of product do not match'

    def basket_price_should_be_correct(self):
        # Проверка на совпадение цены товара на общую цену корзины
        price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert self.product_price == price, 'Price does not match with basket total'

    def should_be_successfully_added_to_basket(self):
        # Сет проверок на успешное добавление товара в корзину
        self.success_messages_should_appear_after_product_added()
        self.product_names_should_match()
        self.basket_price_should_be_correct()

    def success_messages_should_appear_after_product_added(self):
        # Проверка наличия сообщений об умпешном добавлении товара
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES)

    def success_messages_should_disappear(self):
        # отрицательная проверка на то, что сообщения об успешном добавлении исчезли
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_NAME), 'Elements not disappeared, but should'

    def should_not_be_success_messages(self):
        # Отрицательная проверка на то, что после успешного добавления сообщения не появились
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), 'Success messages present, but should not'
