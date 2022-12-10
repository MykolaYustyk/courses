'''2. Написати програму, яка має складатися з трьох файлів/модулів. - rozetka_api.py, де створти клас RozetkaAPI,
який буде містити 1 метод get_item_data, який на вхід отримує id товара з сайту розетки та повертає словник з такими
даними: item_id (він же і приймається на вхід), title, old_price, current_price, href (лінка на цей товар на сайті),
brand, category. Всі інші методи, що потрібні для роботи мають бути приватні/захищені. - data_operations.py з класами
CsvOperations та DataBaseOperations. CsvOperations містить метод для читання даних. Метод для читання приймає
аргументом шлях до csv файлу де в колонці ID записані як валідні, так і не валідні id товарів з сайту.
DataBaseOperations містить метод для запису даних в sqlite3 базу і відповідно приймає дані для запису. Всі інші
методи, що потрібні для роботи мають бути приватні/захищені. - task.py - головний модуль, який ініціалізує і запускає
весь процес. Суть процесу: читаємо ID товарів з csv файлу, отримуємо необхідні дані і записуємо їх в базу. Якщо ID не
валідний/немає даних - вивести відповідне повідомлення і перейти до наступного. '''
from data_operations import CsvOperation, DataBaseOperation


def main():
    file_csv_name = input('Введіть назву файла з номерами товарів: ')
    csv1 = CsvOperation(file_csv_name)
    result = csv1.read_id_from_csv()
    db1 = DataBaseOperation('rozetka_goods.db')
    db1.create()
    db1.write_info_into_data_base(result)


if __name__ == '__main__':
    main()
