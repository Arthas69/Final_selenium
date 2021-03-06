import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose a language to use: en, es, ru...')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture
def locale(request):
    language = request.config.getoption('language')
    return language


@pytest.fixture
def browser(request, locale):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = FirefoxProfile()
        fp.set_preference('intl.accept_languages', locale)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('Browser should be chrome or firefox')
    yield browser

    browser.quit()
