from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super(LoginPage, self).__init__(browser, url)

    def register_new_user(self, email, password):
        # Регистрация нового пользователя
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

        confirmation_input = self.browser.find_element(*LoginPageLocators.CONFIRMATION_INPUT)
        confirmation_input.send_keys(password)

        # Нажатие на кнопку регистрации
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        # Проверка на правильность перехода на страницу логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка корректности ссылки
        assert 'login' in self.url

    def should_be_login_form(self):
        # Проверка наличия формы авторизации
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        # Проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form not found'
