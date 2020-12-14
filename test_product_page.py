from string import ascii_lowercase
from random import choice

import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail(reason='Bug here!')
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]


def test_guest_should_see_login_link_on_product_page(browser):
    # Наличие кнопки на экране товара
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Переход на страницу авторизации со страницы товара
    page = ProductPage(browser, product_link)
    page.open()
    browser = page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Отрицательный тест на наличие сообщений об успехе после добавления товара для ГОСТЯ
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_messages()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Отрицательный тесть на пропадающие сообщения об успехе добавления товара
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.success_messages_should_disappear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # После перехода на страницу корзины со страницы товара, проверка на то, что корзина пустая
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_basket_link()

    browser = page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # Гость может добавить товар в корзину
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successfully_added_to_basket()


@pytest.mark.user_auth
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = ''.join((choice(ascii_lowercase) for _ in range(6))) + '@mail.org'
        password = 'qetuo[adgjl'
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Отрицательный тест на наличие сообщений об успехе после добавления товара для ПОЛЬЗОВАТЕЛЯ
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_messages()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Пользователь может добавлять товар в корзину
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_be_successfully_added_to_basket()
