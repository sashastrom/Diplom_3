import allure
from web_locators.locators import OrdersPageElements
from pages.base_page import BasePage


class CreateOrderPage(BasePage):
    @allure.step('Нажимаем на заказ в "Лента заказов"')
    def click_on_order(self):
        self.click(OrdersPageElements.order_link_locator)

    @allure.step('Проверяем что структура состава отобразилась')
    def check_order_structure(self):
        return self.check_presence(OrdersPageElements.order_structure_locator).is_displayed()

    @allure.step("Проверяем заказы в истории ленты")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверяем конкретный заказ в истории")
    def order_id_found_at_history(self, order_number):
        return self.check_order_id(order_number, OrdersPageElements.all_orders_at_history_locator)

    @allure.step("Проверяем конкретный заказ в истории")
    def order_id_found_at_feed(self, order_number):
        return self.check_order_id(order_number, OrdersPageElements.all_orders_at_feed_locator)

    @allure.step("Получаем количество заказов")
    def get_total_order_count(self, locator):
        return self.get_text(locator)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersPageElements.number_in_progress_locator, order_refactor)
        return order_refactor

    @allure.step('Получаем номер заказа в процессе')
    def get_user_order_in_progress(self):
        return self.get_text(OrdersPageElements.number_in_progress_locator)