from .main_page import MainPage
from .locators import BasketPageLocators


class BasketPage(MainPage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_empty_basket(self):
        # Проверка, является ли корзина пустой
        self.should_be_basket_page()
        self.basket_should_not_contain_items()
        self.text_should_tell_basket_is_empty()

    def should_be_basket_page(self):
        # Корректна ли ссылка на страницу корзины
        assert 'basket' in self.url, 'Basket page url does not contains word "basket"'

    def basket_should_not_contain_items(self):
        # Есть или нет товары в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'The basket is not empty'

    def text_should_tell_basket_is_empty(self):
        # Если корзина пустая на странице должэен быть текст "Your basket is empty."
        empty_basket_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text.strip()
        assert 'Your basket is empty.' in empty_basket_text, 'The basket is not empty'
