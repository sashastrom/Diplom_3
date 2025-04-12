import time
from data.personal_data import LoginData
from conftest import *


class TestRecoveryPassword:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_password_reset_button(self, pages):
        pages.click_on_account()
        pages.wait_for_login_page()
        pages.click_password_reset_link()
        current_url = pages.get_current_url()
        assert current_url == Urls.restore_url

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_reset(self, pages):
        pages.open_url(Urls.restore_url)
        pages.fill_email_for_reset_password(LoginData.email)
        pages.click_reset_button()
        pages.find_save_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.reset_url

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_make_field_active(self, pages):
        pages.open_url(Urls.restore_url)
        pages.fill_email_for_reset_password(LoginData.email)
        pages.click_reset_button()
        pages.find_save_button()
        time.sleep(1)
        pages.click_on_show_password_button()
        time.sleep(1)
        assert pages.find_input_active()