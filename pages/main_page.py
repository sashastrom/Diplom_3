import time
import allure
from web_locators.locators import MainPageElements, OrdersPageElements
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на "Личный кабинет"')
    def click_on_account(self):
        self.click(MainPageElements.profile_button_locator)

    @allure.step('Переход на страницу "Лента Заказов"')
    def click_orders_list_button(self):
        self.move_to_element(MainPageElements.orders_list_button_locator)
        time.sleep(4)
        self.wait_until_element_visibility(OrdersPageElements.order_link_locator)
        time.sleep(4)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.click(MainPageElements.constructor_button_locator)
        self.wait_until_element_visibility(MainPageElements.main_list_title_locator)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageElements.bun_ingredient_locator)
        time.sleep(2)
        self.click(MainPageElements.bun_ingredient_locator)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageElements.ingredient_details_popup_locator)
        return self.get_text(MainPageElements.ingredient_details_popup_locator)

    @allure.step('Закрыть - (клик на крестик)')
    def click_cross_button(self):
        self.move_to_element(MainPageElements.close_button_locator)

    @allure.step('Проверяем что детали ингредиентов скрыты')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageElements.ingredient_details_popup_locator)

    @allure.step('Проверяем что наличие ингредиентов отобразилось')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presence(MainPageElements.ingredient_details_popup_locator).is_displayed()

    @allure.step('Проверяем счетчик ингредиентов')
    def get_count_value(self):
        time.sleep(3)
        return self.get_text(MainPageElements.ingredient_counter_locator)

    @allure.step('Добавляем ингридиент в заказ')
    def add_filling_to_order(self):
        time.sleep(2)
        self.wait_for_element_to_be_clickable(MainPageElements.bun_ingredient_locator)
        time.sleep(2)
        self.drag_and_drop(MainPageElements.bun_ingredient_locator, MainPageElements.order_basket_locator)
        time.sleep(2)

    @allure.step('Клик на кнопку "Оформить Заказ"')
    def click_order_button(self):
        self.move_to_element(MainPageElements.create_order_button_locator)

    @allure.step('Проверяем окно с номером заказа')
    def check_show_window_with_order_id(self):
        self.wait_until_element_visibility(MainPageElements.order_identify_locator)
        return self.get_text(MainPageElements.order_identify_locator)

    @allure.step('Получаем ID заказа')
    def get_with_order_id(self):
        self.wait_until_element_visibility(MainPageElements.order_identify_locator)
        order_id = self.get_text(MainPageElements.order_id_locator)
        while order_id == '9999':
            order_id = self.get_text(MainPageElements.order_id_locator)
        return f"{order_id}"

    @allure.step("Проверяем модальное окно")
    def modal_box_is_open(self):
        if self.find_elements(MainPageElements.close_modal_order_locator):
            return True

    @allure.step('Проверяем статус заказа')
    def check_displayed_order_status_text(self) -> bool:
        return self.check_presence(MainPageElements.order_status_text_locator).is_displayed()

    @allure.step("Закрываем модальное окно после заказа")
    def click_close_modal_order(self):
        self.wait_until_element_visibility(MainPageElements.close_modal_order_locator)
        self.click(MainPageElements.close_modal_order_locator)