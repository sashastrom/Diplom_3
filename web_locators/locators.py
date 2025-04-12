from selenium.webdriver.common.by import By


class MainPageElements:
    profile_button_locator = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    login_profile_button_locator = By.XPATH, ".//button[text()='Войти в аккаунт']"
    constructor_button_locator = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    main_list_title_locator = By.XPATH, "//h1[text()='Соберите бургер']"
    orders_list_button_locator = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    bun_ingredient_locator = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    ingredient_details_popup_locator = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    close_button_locator = By.XPATH, '//button[contains(@class,"close")]'
    ingredient_counter_locator = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    order_basket_locator = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    create_order_button_locator = By.XPATH, '//button[text()="Оформить заказ"]'
    order_identify_locator = (By.XPATH, '//p[text()="идентификатор заказа"]')
    order_id_locator = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    loading_check_box_locator = (By.XPATH, ".//img[@alt='tick animation']")
    order_status_text_locator = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    close_modal_order_locator = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    main_order_h1_locator = (By.XPATH, ".//p[text()='Соберите бургер']")
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")


class AuthLoginElements:
    email_field_locator = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    password_field_locator = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    login_button_any_forms_locator = (By.XPATH, ".//button[text()='Войти']")
    forgot_password_link_locator = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
    logout_text_locator = (By.XPATH, '//button[contains(text(), "Выход")]')


class AuthForgotPasswordElements:
    input_email_field_locator = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    reset_button_locator = (By.XPATH, '//button[text()="Восстановить"]')
    input_active_field_locator = (By.CSS_SELECTOR, '.input.input_status_active')
    show_password_button_locator = (By.XPATH, '//div[contains(@class,"icon-action")]')
    save_button_locator = (By.XPATH, '//button[text()="Сохранить"]')


class UserProfileElements:
    profile_button_locator = (By.LINK_TEXT, 'Профиль')
    order_history_button_locator = (By.LINK_TEXT, 'История заказов')
    enabled_order_history_button_locator = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')
    logout_button_locator = (By.XPATH, ".//button[text()='Выход']")
    lk_info_message_locator = (By.XPATH, ".//p[contains(text(),'персональные данные')]")


class OrdersPageElements:
    orders_list_title_locator = (By.XPATH, '//h1[text()="Лента заказов"]')
    order_structure_locator = (By.XPATH, '//p[text()="Cостав"]')
    order_link_locator = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    all_orders_at_history_locator = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")
    all_orders_at_feed_locator = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']")
    total_order_count_locator = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    daily_order_count_locator = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    number_in_progress_2_locator = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')
    number_in_progress_locator = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
