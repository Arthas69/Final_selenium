from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super(LoginPage, self).__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form not found'
