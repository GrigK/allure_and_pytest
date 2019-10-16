from faker import Faker
import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


# [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]
@pytest.mark.need_review
@pytest.mark.parametrize('suffix', (no if no != 7 else pytest.param(no, marks=pytest.mark.xfail) for no in range(10)))
def test_guest_can_add_product_to_basket(browser, suffix):
    uri = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{suffix}"
    page = ProductPage(browser, uri)
    page.open()
    page.add_product_to_basket_and_calculate()


@pytest.mark.xfail
def test_guest_cant_see_success_message_    after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()
    page.add_product_to_basket_and_calculate()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.is_disappered_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_basket()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:
    password = 'Qw21eR4t50'
    faker: Faker = Faker(locale='ru-RU')

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
            открыть страницу регистрации
            зарегистрировать нового пользователя
            проверить, что пользователь залогинен

            так обычно не делают в setup это просто для примера
        """
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(self.faker.email(), self.password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_btn_basket()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_and_calculate()
