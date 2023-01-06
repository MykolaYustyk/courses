"""1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv". Увага! Файл має бути
прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально.
 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
 3. Перейдіть у вкладку "Order your robot"
 4. Для кожного замовлення з файлу реалізуйте наступне:
  - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
  - оберіть/заповніть відповідні поля для замовлення
  - натисніть кнопку Preview та збережіть зображення отриманого робота.
   Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
  - натисніть кнопку Order та збережіть номер чеку.
   Увага! Інколи сервер тупить і видає помилку, але повторне натискання кнопки частіше всього
   вирішує проблему. Дослідіть цей кейс.
  - переіменуйте отримане зображення у формат <номер чеку>_robot.
    Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
  - замовте наступного робота (шляхом натискання відповідної кнопки)

"""
import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def create_output_folder():
    if not (os.path.exists('output')):
        os.mkdir('output')
    else:
        os.system('cd output')
        for file in os.scandir(os.path.abspath('output')):
            os.unlink(file.path)


def read_csv(driver):
    robot_input = []
    csvfile = requests.get('https://robotsparebinindustries.com/orders.csv')
    temp = csvfile.text.split('\n')
    for robot in temp[1:]:
        robot_input.append(robot.split(","))
    return robot_input


def click_order_your_robot(driver):
    driver.get('https://robotsparebinindustries.com/')
    order_robot_button = driver.find_element(By.CSS_SELECTOR, 'a.nav-link')
    order_robot_button.click()


def set_robot_parts(driver, robot):
    driver.get('https://robotsparebinindustries.com/#/robot-order')
    button_ok = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[2]')
    button_ok.click()
    head = Select(driver.find_element(By.NAME, 'head'))
    head.select_by_value(f'{robot[1]}')
    robot_body = driver.find_element(By.ID, f'id-body-{robot[2]}')
    robot_body.click()
    robot_legs = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    robot_legs.send_keys(f'{robot[3]}')
    robot_address = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    robot_address.click()
    robot_address.send_keys(f'{robot[4]}')


def preview_robot(driver):
    button_preview = driver.find_element(By.CSS_SELECTOR, 'button[id="preview"]')
    button_preview.click()


def save_robot_picture(driver, robot):
    robot_picture = driver.find_element(By.CSS_SELECTOR, 'div[id="robot-preview-image"]')
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div[id="robot-preview-image"]')))
    file_name = f'{robot[0]}.png'
    robot_picture.screenshot(f'output/{file_name}')
    return file_name


def click_button_order(driver):
    while True:
        try:
            button_order = WebDriverWait(driver, 2)
            button_order.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
            receipt = WebDriverWait(driver, 2)
            check_receipt = receipt.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'alert-success'))).is_displayed()
            if check_receipt:
                break
        except TimeoutException:
            continue


def rename_robot_file(driver, file):
    new_name = driver.find_element(By.XPATH, '//*[@id="receipt"]/p[1]').text
    os.rename(f'output/{file}', f'output/{new_name}.png')


def order_another_robot(driver):
    button_order_another_robot = driver.find_element(By.CSS_SELECTOR, 'button[id="order-another"]')
    button_order_another_robot.click()


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    create_output_folder()
    list_of_robots = read_csv(driver)
    click_order_your_robot(driver)
    for robot in list_of_robots:
        set_robot_parts(driver, robot)
        preview_robot(driver)
        current_robot = save_robot_picture(driver, robot)
        click_button_order(driver)
        rename_robot_file(driver, current_robot)
        order_another_robot(driver)
    driver.quit()


if __name__ == '__main__':
    main()
