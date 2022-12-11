import csv
import sqlite3

from rozetka_api import RozetkaAPI


class CsvOperation:

    @staticmethod
    def read_id_from_csv(row_dict):
        return int(row_dict['id'])


class SiteParser:

    def __init__(self, file_name):
        self.file_name = file_name

    @property
    def get_list_of_goods(self):
        return self._parse_goods()

    def _parse_goods(self):
        list_of_goods = []
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',', fieldnames=['id'])
            reader = list(reader)
            for row in reader[1:]:
                item_id = CsvOperation.read_id_from_csv(row)
                good = RozetkaAPI.get_item_data(item_id)
                if good['price'] == 0:
                    print(f'Сайт не містить інформацію про товар з номером {good["item_id"]}')
                else:
                    print(f'Товар № {good["item_id"]} заноситься в базу даних')
                    list_of_goods.append(good)
        return list_of_goods


class DataBaseOperation:

    def __init__(self, data_base_file_name, items_list):
        self.data_base_file_name = data_base_file_name
        self.items_list = items_list

    def _create(self):
        with sqlite3.connect(self.data_base_file_name) as con:
            cursor = con.cursor()
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS goods_info(
                id INTEGER,
                title TEXT,
                price INTEGER,
                old_price INTEGER,
                href TEXT,
                brand TEXT,
                category TEXT
                ) ''')
            con.commit()

    def write_info_into_data_base(self):
        self._create()
        with sqlite3.connect(self.data_base_file_name) as con:
            cursor = con.cursor()
            for good in self.items_list:
                cursor.execute(""" INSERT INTO goods_info
                                    VALUES(?, ?, ?, ?, ?, ?, ?)""",
                               (good['item_id'], good['title'], int(good['price']),
                                int(good['old_price']), good['href'], good['brand'],
                                good['category'])
                               )
                con.commit()


if __name__ == "__main__":
    parser = SiteParser('test.csv')
    goods_list = parser.get_list_of_goods
    db1 = DataBaseOperation('rozetka_goods.db', goods_list)
    db1.write_info_into_data_base()
