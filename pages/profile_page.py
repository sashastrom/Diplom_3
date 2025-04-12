import allure
from web_locators.locators import UserProfileElements
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step('Проверяем переход на страницу профиля')
    def switch_on_profile(self):
        self.wait_until_element_visibility(UserProfileElements.profile_button_locator)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(UserProfileElements.order_history_button_locator)
        self.click(UserProfileElements.order_history_button_locator)

    @allure.step('Проверяем переход на страницу История заказов')
    def switch_on_order_history(self):
        self.wait_until_element_visibility(UserProfileElements.enabled_order_history_button_locator)
        return self.get_current_url()

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.wait_for_element_to_be_clickable(UserProfileElements.logout_button_locator)
        self.click(UserProfileElements.logout_button_locator)