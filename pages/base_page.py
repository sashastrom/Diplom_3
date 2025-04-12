import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем ссылку')
    def open_url(self, url):
        return self.driver.get(url)

    @allure.step('Кликаем по элементу {locator}')
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            WebDriverWait(self.driver, 5).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
        except TimeoutException:
            pass
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step('Вставить текст {text}')
    def send_text_key(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текущий текст')
    def get_text(self, locator):
        actual_text = self.driver.find_element(*locator).text
        return actual_text

    @allure.step('Проверить присутствие элемента на странице')
    def check_presence(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_until_element_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, locator_one, locator_two):
        source = self.driver.find_element(*locator_one)
        target = self.driver.find_element(*locator_two)
        self.driver.execute_script("""
            function triggerDragAndDrop(sourceNode, destinationNode) {
                const dataTransfer = new DataTransfer();
                const dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                });
                sourceNode.dispatchEvent(dragStartEvent);

                const dragEnterEvent = new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                });
                destinationNode.dispatchEvent(dragEnterEvent);

                const dragOverEvent = new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                });
                destinationNode.dispatchEvent(dragOverEvent);

                const dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                });
                destinationNode.dispatchEvent(dropEvent);

                const dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer,
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            triggerDragAndDrop(arguments[0], arguments[1]);
        """, source, target)

    @allure.step('Переместиться до элемента и кликнуть')
    def move_to_element(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элементы на странице')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Дождаться появления текста в элементе')
    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(locator))