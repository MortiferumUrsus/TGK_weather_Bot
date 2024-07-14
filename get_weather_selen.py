from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time

# Создание параметров для открытия без окна браузера
def create_driver():
    # Настройка опций Firefox
    options = Options()
    options.add_argument("--headless")  # Включение headless режима
    options.add_argument("--disable-gpu")  # Отключение использования GPU (для стабилизации работы)

    # Инициализация веб-драйвера без указания пути (если geckodriver в PATH)
    driver = webdriver.Firefox(options=options)

    return driver

def open_more_info(driver):
    # Вывод дополнительных данных
    open_dop_info = driver.find_element(By.CLASS_NAME, "weather-parameters-dataset.js-dataset-button")
    open_dop_info.click()
    # Найдите элемент с использованием XPath
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Относительная влажность']]"))
    )
    # Прокрутите элемент в видимую область с помощью JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    # Нажмите на элемент с помощью JavaScript, чтобы избежать проблем с видимостью
    driver.execute_script("arguments[0].click();", button)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(1)

def make_immage(url, city):
    # Создание экземпляра веб-драйвера
    driver = create_driver()

    # Открыть нужную веб-страницу
    driver.get(url)

    # Установка размера окна, чтобы охватить всю высоту страницы
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1200, total_height)

    #Открываем нужную дополнительную информацию
    open_more_info(driver)

    # Установка размера окна, чтобы охватить всю высоту страницы
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1200, total_height)

    # Выбор элемента для захвата (используйте любой подходящий метод поиска элементов)
    element = driver.find_element(By.CLASS_NAME, 'widget-items.js-scroll-item')

    # Захват снимка экрана
    screenshot_path = f'saved_images/full_screenshot_{city}.png'
    driver.save_screenshot(screenshot_path)

    # Получение размеров и координат элемента
    location = element.location
    size = element.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    # Обрезка полной снимка до области элемента с использованием Pillow
    image = Image.open(screenshot_path)
    cropped_image = image.crop((left, top, right, bottom))

    # Сохранение обрезанного изображения
    cropped_screenshot_path = f'saved_images/cropped_screenshot_{city}.png'
    cropped_image.save(cropped_screenshot_path)

    # Закрытие WebDriver
    driver.quit()

