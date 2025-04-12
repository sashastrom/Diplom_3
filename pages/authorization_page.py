import time
from data.personal_data import LoginData
from web_locators.locators import AuthLoginElements, MainPageElements
from pages.base_page import BasePage
import allure

class AuthUserPage(BasePage):

    @allure.step('Переходим в "Войти в аккаунт"')
    def move_to_personal_account_button(self):
        self.move_to_element(MainPageElements.login_profile_button_locator)

    @allure.step('Ждем появления елемента на "забыли пароль"')
    def wait_for_login_page(self):
        self.wait_until_element_visibility(AuthLoginElements.forgot_password_link_locator)

    @allure.step('Заполняем поле "email"')
    def fill_email_field(self, user_email):
        self.wait_until_element_visibility(AuthLoginElements.email_field_locator)
        time.sleep(3)
        self.click(AuthLoginElements.email_field_locator)
        self.send_text_key(AuthLoginElements.email_field_locator, user_email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_field(self, user_password):
        self.click(AuthLoginElements.password_field_locator)
        self.send_text_key(AuthLoginElements.password_field_locator, user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click(AuthLoginElements.login_button_any_forms_locator)

    @allure.step('Авторизируемся')
    def login(self):
        self.move_to_personal_account_button()
        time.sleep(4)
        self.fill_email_field(LoginData.email)
        time.sleep(4)
        self.fill_password_field(LoginData.password)
        time.sleep(4)
        self.click_login_button()
        time.sleep(4)

    @allure.step('Проверяем переход на страницу Авторизации')
    def check_switch_on_login_page(self):
        self.wait_until_element_visibility(AuthLoginElements.logout_text_locator)
        return self.get_current_url()