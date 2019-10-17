import allure
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def add_product_to_basket_and_calculate(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_description()
        self.should_be_add_button()
        self.should_not_be_success_message()

        self.add_product_to_basket()
        self.solve_quiz_and_get_code()

        self.should_be_success()
        self.check_success_message()

    @allure.step("Добавим товара в корзину")
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    @allure.step("Сообщение о добавлении товара должно исчезнуть")
    def is_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    @allure.step("Прочитаем название товара")
    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    @allure.step("Прочитаем стоимость товара")
    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    @allure.step("Прочитаем описание товара")
    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    @allure.step("Сообщение о добавлении товара в корзину присутствует")
    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                               "basket not found "

    @allure.step("Не должно быть сообщения о добавлении товара")
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    @allure.step("Кнопка добавления товара присутствует на странице")
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                "presented "

    @allure.step("Проверим наличие сообщения об успешном добавлении товара в корзину")
    def check_success_message(self):
        msg_lst = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)
        assert len(msg_lst) == 3, "Success message not found"

        assert self.product_name == msg_lst[0].text, "Wrong name product added to basket"
        assert self.product_price == msg_lst[2].text, "Wrong price product added to basket"
