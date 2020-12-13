import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    @staticmethod
    def _solve(x):
        return str(math.log(abs(12 * math.sin(float(x)))))

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            alert = self.browser.switch_to.alert
        except NoAlertPresentException:
            return False
        return alert

    def solve_quiz_and_get_code(self):
        alert = self.is_alert_present()
        if not alert:
            print('No promo alert!')
            return
        x = alert.text.split(' ')[2]
        answer = self._solve(x)
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f'Your code: {alert_text}')
        #     alert.accept()
        #     time.sleep(120)
        # except NoAlertPresentException:
        #     print('No second alert presented')
