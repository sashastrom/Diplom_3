import allure
from web_locators.locators import AuthForgotPasswordElements, AuthLoginElements
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажимаем на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click(AuthLoginElements.forgot_password_link_locator)

    @allure.step('Вводим email в поле для восстановления пароля')
    def fill_email_for_reset_password(self, email):
        self.send_text_key(AuthForgotPasswordElements.input_email_field_locator, email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_reset_button(self):
        self.move_to_element(AuthForgotPasswordElements.reset_button_locator)

    @allure.step('Кликаем на кнопку "Показать/Cкрыть пароль"')
    def click_on_show_password_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )
        self.click(AuthForgotPasswordElements.show_password_button_locator)

    @allure.step('Находим и ждем кнопку "Сохранить"')
    def find_save_button(self):
        self.wait_until_element_visibility(AuthForgotPasswordElements.save_button_locator)

    @allure.step('Находим поле "Пароль"')
    def find_input_active(self):
        return self.wait_until_element_visibility(AuthForgotPasswordElements.input_active_field_locator)