import math
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (NoSuchElementException, NoAlertPresentException,
                                        TimeoutException)

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    @staticmethod
    def _solve(x):
        return str(math.log(abs(12 * math.sin(float(x)))))

    def open(self):
        # Открыть страницу
        self.browser.get(self.url)

    def go_to_login_page(self):
        # Перейти на страницу авторизации
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        return self.browser

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        return self.browser

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            'User icon not presented? probably unauthorized user'

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not presented'

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), 'Basket link is not presented'

    def is_alert_present(self):
        # Проверить наличие alert'а на странице
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            return False
        return alert

    def is_disappeared(self, how, what, timeout=4):
        # Ждать пока элемент не исчезнет - если не исчез, бросить исключение
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        # Проверить НАЛИЧИЕ элемента на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # Проверить ОТСУТСТВИЕ элемента на странице
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def solve_quiz_and_get_code(self):
        alert = self.is_alert_present()
        if not alert:
            print('No promo alert!')
            return
        x = alert.text.split(' ')[2]
        answer = self._solve(x)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
            # time.sleep(120)
        except NoAlertPresentException:
            print('No second alert presented')
