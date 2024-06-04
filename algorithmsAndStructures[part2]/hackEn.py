from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Путь к chromedriver
path_to_chromedriver = 'C:\\Users\\Firo\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

# Настройка опций Chrome для удаленного управления
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9515")

# Подключение к уже запущенному Chrome
service = Service(executable_path=path_to_chromedriver)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL целевой страницы
target_url = "https://lms.kantiana.ru/mod/hvp/view.php?id=341872"
driver.get(target_url)

# Ожидание полной загрузки страницы
time.sleep(5)  # Подождем 5 секунд для полной загрузки страницы

def select_checkbox_and_check():
    try:
        # Найти все чекбоксы (укажите правильный XPath для чекбоксов)
        checkboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//input[@type="checkbox"]'))
        )
        print(f"Найдено {len(checkboxes)} чекбоксов.")

        for checkbox in checkboxes:
            try:
                print("Выбираем чекбокс.")
                # Выбрать чекбокс
                checkbox.click()

                # Нажать на кнопку "Проверить" (укажите правильный XPath для кнопки "Проверить")
                check_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Проверить")]'))
                )
                print("Нажимаем кнопку 'Проверить'.")
                check_button.click()

                time.sleep(2)  # Ждать, чтобы результат обновился

                # Проверить результат (укажите правильный XPath для элемента результата)
                result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="result"]'))
                )
                print(f"Результат проверки: {result.text}")
                if "успешно" in result.text.lower():
                    print("Ответ верный. Нажимаем кнопку 'Продолжить'.")
                    # Если успешно, нажать кнопку "Продолжить" (укажите правильный XPath для кнопки "Продолжить")
                    continue_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Продолжить")]'))
                    )
                    continue_button.click()
                    return True
                else:
                    print("Ответ неверный. Снимаем галочку.")
                    # Если неверно, снять галочку и перейти к следующей
                    checkbox.click()
            except Exception as e:
                print(f"Ошибка при взаимодействии с чекбоксом: {e}")
                continue
    except Exception as e:
        print(f"Ошибка при поиске чекбоксов: {e}")

    return False

# Запуск функции выбора чекбоксов и проверки
success = select_checkbox_and_check()
if success:
    print("Операция завершена успешно!")
else:
    print("Не удалось выполнить операцию.")

# Закрыть браузер
driver.quit()
