from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super(ProductPage, self).__init__(browser, url)
        self.product_name = None
        self.product_price = None

    def add_product_to_basket(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_button_on_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON)

    def should_be_successfully_added_to_basket(self):
        self.should_be_visible_messages_of_successful_addition()
        self.should_be_concurrent_names_of_added_book()
        self.should_be_correct_basket_price()

    def should_be_visible_messages_of_successful_addition(self):
        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGES)

    def should_be_concurrent_names_of_added_book(self):
        name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        assert self.product_name == name, 'The names of product do not match'

    def should_be_correct_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text
        assert self.product_price == price, 'Price does not match with basket total'
