import csv
import sqlite3

from dataclasses import dataclass

from rozetka_api import RozetkaAPI


@dataclass
class CsvOperation:

    _file_name: str = ''

    @property
    def __file_name(self):
        return self._file_name

    @__file_name.setter
    def __file_name(self, name):
        self._file_name = name

    def read_id_from_csv(self):
        result = []
        with open(self._file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',', fieldnames=['id'])
            reader = list(reader)
            for row in reader[1:]:
                item_id = int(row['id'])
                current_item = RozetkaAPI(item_id)
                result.append(current_item.get_item_data(item_id))
        return result

@dataclass
class DataBaseOperation:

    _data_base_file_name: str = ''

    @property
    def __data_base_file_name(self):
        return self._data_base_file_name
    
    @__data_base_file_name.setter
    def __data_base_file_name(self, name):
        self._data_base_file_name = name
    
    def create(self):
        with sqlite3.connect(self.__data_base_file_name) as con:
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
            
    def write_info_into_data_base(self, goods_list):
        with sqlite3.connect(self.__data_base_file_name) as con:
            cursor = con.cursor()
            for good in goods_list:
                if good['price'] == '0' or good['price'] == '':
                    print(f'Сайт не містить інформацію про товар з номером {good["item_id"]}')
                else:
                    print(f'Товар № {good["item_id"]} заноситься в базу даних')
                    cursor.execute(""" INSERT INTO goods_info
                                    VALUES(?, ?, ?, ?, ?, ?, ?)""",
                                   (good['item_id'], good['title'], int(good['price']),
                                    int(good['old_price']), good['href'], good['brand'],
                                    good['category'])
                                   )
                    con.commit()
            
            

if __name__ == "__main__":
    csv1 = CsvOperation('test.csv')
    result = csv1.read_id_from_csv()
    db1 = DataBaseOperation('rozetka_goods.db')
    db1.create()
    db1.write_info_into_data_base(result)
