import pytest
import allure

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


@allure.feature('Тесты для Гостя')
@allure.story('Несколько тестов для примера')
@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """
        Гость может перейти на страницу логина
        """
        with allure.step("Открываем главную страницу"):
            page = MainPage(browser, link)
            page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.feature('Guest can see product in mini-basket from main page')
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """
        Гость при заходе в корзину с главной страницы
        Должен увидеть что корзина пуста
        """
        with allure.step("Открываем главную страницу"):
            page = MainPage(browser, link)
            page.open()
        page.should_be_btn_basket()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    @allure.feature('Guest can goto login page')
    def test_guest_goto_login_page(self, browser):
        """
        Гость может перейти на страницу логина
        """
        with allure.step("Открываем главную страницу"):
            page = MainPage(browser, link)
            page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.step("Гость должен видеть login link")
    def test_guest_should_see_login_link(self, browser):
        """
        Гость всегда может видеть ссылку на вход и регистрацию на сайте
        """
        with allure.step("Открываем главную страницу"):
            page = MainPage(browser, link)
            page.open()
        page.should_be_login_link()
