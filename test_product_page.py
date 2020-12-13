import pytest

from pages.product_page import ProductPage


product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

links_xfail = links.copy()
links_xfail[7] = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successfully_added_to_basket()


@pytest.mark.parametrize('link', links)
def test_add_button_is_visible(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_on_page()
    page.should_not_be_success_messages()


@pytest.mark.parametrize('link', links_xfail)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_successfully_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_messages()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_messages()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_messages()


# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_successfully_added_to_basket()
