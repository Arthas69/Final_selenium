from .base_page import BasePage
from .locators import MainPageLocator


class MainPage(BasePage):

    def __init__(self, browser, url):
        super(MainPage, self).__init__(browser, url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocator.LOGIN_LINK)
        login_link.click()
        return self.browser

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), 'Login link is not presented'
