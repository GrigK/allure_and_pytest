import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    для запуска :
        pytest -s -v --tb=short --browser_name=firefox test_conftest.py
        pytest -s -v --tb=short --browser_name=chrome --language=en test_conftest.py
    по умолчанию броузер 'chrome' и язык 'en'
        pytest -s -v --tb=line test_main_page.py
        pytest -s -v --alluredir=reports --tb=short test_main_page.py
        ~/allure/bin/allure serve reports
    """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language browser: ru,en,es... (default - en)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
