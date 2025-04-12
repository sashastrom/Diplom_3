import time
import allure
from conftest import *
from web_locators.locators import OrdersPageElements


class TestCreateOrder:
    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_get_order_popup(self, pages):
        pages.click_orders_list_button()
        pages.click_on_order()
        assert pages.check_order_structure() == True

    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_find_order_in_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.check_show_window_with_order_id()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_on_account()
        pages.click_order_history_button()
        order_id_found_at_history = pages.order_id_found_at_history(order_number)
        pages.click_orders_list_button()
        order_id_found_at_feed = pages.order_id_found_at_feed(order_number)
        assert order_id_found_at_history and order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('Проверяем что при создании нового заказа счётчик "Выполнено за всё время" и "Выполнено за сегодня" увеличивается')
    @pytest.mark.parametrize('counter', [OrdersPageElements.total_order_count_locator, OrdersPageElements.daily_order_count_locator])
    def test_today_orders_counter(self, pages, login, counter):
        pages.click_orders_list_button()
        prev_counter_value = pages.get_total_order_count(counter)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        time.sleep(3)
        pages.click_close_modal_order()
        time.sleep(4)
        pages.click_orders_list_button()
        current_counter_value = pages.get_total_order_count(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"

    @allure.title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_work_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        order_number_refactor = pages.get_user_order(order_number)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress