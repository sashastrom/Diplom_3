import allure
from conftest import *



class TestPersonalArea:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_go_to_personal_area(self, pages, login):
        pages.click_on_account()
        current_url = pages.check_switch_on_login_page()
        assert current_url == Urls.profile_url

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_go_to_order_history(self, pages, login):
        pages.click_on_account()
        pages.click_order_history_button()
        current_url = pages.switch_on_order_history()
        assert current_url == Urls.order_history_url

    @allure.title('Проверяем выход из аккаунта.')
    def test_logout(self, pages, login):
        pages.click_on_account()
        pages.click_log_out_button()
        current_url = pages.check_switch_on_login_page()
        assert current_url == Urls.profile_url