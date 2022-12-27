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
import time
import os
import csv


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC




def read_csv(driver):
    driver.get('https://robotsparebinindustries.com/orders.csv')
    robot_input = []
    with open(f'{os.path.abspath("orders.csv")}', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for robot in reader:
            robot_input.append(robot)
    return robot_input


def click_order_your_robot(driver):
    driver.get('https://robotsparebinindustries.com/')
    order_robot_button = driver.find_element(By.CSS_SELECTOR, 'a.nav-link')
    order_robot_button.click()
    time.sleep(1)


def set_robot_parties(driver, robot):
    driver.get('https://robotsparebinindustries.com/#/robot-order')
    button_ok = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div/button[2]')
    button_ok.click()
    head = Select(driver.find_element(By.NAME, 'head'))
    head.select_by_value(f'{robot["Head"]}')
    robot_body = driver.find_element(By.ID, f'id-body-{robot["Body"]}')
    robot_body.click()
    robot_legs = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    robot_legs.send_keys(f'{robot["Legs"]}')
    robot_address = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    robot_address.click()
    robot_address.send_keys(f'{robot["Address"]}')


def preview_robot(driver):
    button_preview = driver.find_element(By.CSS_SELECTOR, 'button[id="preview"]')
    button_preview.click()
    time.sleep(2)

def save_robot_picture(driver, robot):
    robot_picture = driver.find_element(By.CSS_SELECTOR, 'div[id="robot-preview-image"]')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="robot-preview-image"]')))
    robot_picture.screenshot(f'robot{robot["Order number"]}.png')

def click_button_order(driver):
    button_order = driver.find_element(By.CSS_SELECTOR, 'button[id="order"]')
    while True:
        button_order.click()
        check_visible = driver.find_element(By.CSS_SELECTOR, 'div[id="receipt"]').is_displayed()
        if check_visible:
            break

def order_another_robot(driver):
    button_order_another_robot = driver.find_element(By.CSS_SELECTOR, 'button[id="order-another"]')
    button_order_another_robot.click()

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    list_of_robots = read_csv(driver)
    click_order_your_robot(driver)
    for robot in list_of_robots:
        set_robot_parties(driver, robot)
        preview_robot(driver)
        save_robot_picture(driver, robot)
        click_button_order(driver)
        order_another_robot(driver)
    driver.quit()


if __name__ == '__main__':
    main()