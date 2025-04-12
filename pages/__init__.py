from pages.authorization_page import AuthUserPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.recover_password_page import PasswordRecoveryPage
from pages.order_page import CreateOrderPage
from pages.profile_page import UserProfilePage

class AllWorkingPages(MainPage, AuthUserPage, PasswordRecoveryPage, UserProfilePage, CreateOrderPage):
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators