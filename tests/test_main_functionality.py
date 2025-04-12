import time
import allure
from conftest import *
from data.urls import Urls


class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_redirection_to_order_list(self, pages):
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.feed_url

    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_go_to_constructor(self, pages):
        pages.click_orders_list_button()
        time.sleep(2)
        pages.click_constructor_button()
        time.sleep(2)
        current_url = pages.get_current_url()
        assert current_url == Urls.main_url

    @allure.title('Проверяет что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_popup_of_ingredient(self, pages):
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('Проверяем что всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window(self, pages):
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    @allure.title('Проверяем что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter(self, pages):
        prev_counter_value = pages.get_count_value()
        pages.add_filling_to_order()
        actual_value = pages.get_count_value()
        time.sleep(5)
        assert actual_value > prev_counter_value

    @allure.title('Проверяем что залогиненный пользователь может оформить заказ.')
    def test_successful_order(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        actually_text = pages.check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and pages.check_displayed_order_status_text() == True