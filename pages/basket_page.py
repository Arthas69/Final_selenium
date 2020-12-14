from .main_page import MainPage
from .locators import BasketPageLocators


class BasketPage(MainPage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket(self):
        self.should_be_basket_page()
        self.should_not_contain_items()
        self.should_be_empty_basket_text()

    def should_be_basket_page(self):
        assert 'basket' in self.url, 'Basket page url does not contains word "basket"'

    def should_not_contain_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'The basket is not empty'

    def should_be_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text.strip()
        assert 'Your basket is empty.' in empty_basket_text, 'The basket is not empty'
