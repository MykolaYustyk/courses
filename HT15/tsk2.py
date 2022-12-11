"""2. Написати програму, яка має складатися з трьох файлів/модулів. - rozetka_api.py, де створти клас RozetkaAPI,
який буде містити 1 метод get_item_data, який на вхід отримує id товара з сайту розетки та повертає словник з такими
даними: item_id (він же і приймається на вхід), title, old_price, current_price, href (лінка на цей товар на сайті),
brand, category. Всі інші методи, що потрібні для роботи мають бути приватні/захищені. - data_operations.py з класами
CsvOperations та DataBaseOperations. CsvOperations містить метод для читання даних. Метод для читання приймає
аргументом шлях до csv файлу де в колонці ID записані як валідні, так і не валідні id товарів з сайту.
DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно приймає дані для запису. Всі інші
методи, що потрібні для роботи мають бути приватні/захищені. - task.py - головний модуль, який ініціалізує і запускає
весь процес. Суть процесу: читаємо ID товарів з csv файлу, отримуємо необхідні дані і записуємо їх в базу. Якщо ID не
валідний/немає даних - вивести відповідне повідомлення і перейти до наступного. """
from data_operations import DataBaseOperation, SiteParser


def main():
    file_csv_name = input('Введіть назву файла з номерами товарів: ')
    parser = SiteParser(file_csv_name)
    goods_list = parser.get_list_of_goods
    db1 = DataBaseOperation('rozetka_goods.db', goods_list)
    db1.write_info_into_data_base()


if __name__ == '__main__':
    main()
