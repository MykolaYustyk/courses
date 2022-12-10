import csv
import sqlite3
import os.path


from rozetka_api import RozetkaAPI


class CsvOperation:
<<<<<<< HEAD
    
    def __init__(self, file_name):
        self.file_name = file_name


    def read_id_from_csv(self):
        result = []
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',', fieldnames=['id'])
=======
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
            reader = csv.DictReader(file, delimiter=',', fieldnames=['_id'])
>>>>>>> 9c26894f9834a366849c6c12a7c14f32f9e7b3b6
            reader = list(reader)
            for row in reader[1:]:
                item_id = int(row['_id'])
                current_item = RozetkaAPI(item_id)
                good = current_item.get_item_data()
                if good['price'] == 0:
                    print(f'Сайт не містить інформацію про товар з номером {good["item_id"]}')
                else:
                    print(f'Товар № {good["item_id"]} заноситься в базу даних')
                    result.append(current_item.get_item_data())
        return result

<<<<<<< HEAD
class DataBaseOperation:

    def __init__(self, data_base_file_name):
        self.data_base_file_name = data_base_file_name
        
    
    def _create(self):
        with sqlite3.connect(self.data_base_file_name) as con:
=======

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
>>>>>>> 9c26894f9834a366849c6c12a7c14f32f9e7b3b6
            cursor = con.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS goods_info(
                id INTEGER,
                title TEXT,
                price INTEGER,
                old_price INTEGER,
                href TEXT,
                brand TEXT,
                category TEXT
                ) ''')
            con.commit()
<<<<<<< HEAD
            
            
=======

>>>>>>> 9c26894f9834a366849c6c12a7c14f32f9e7b3b6
    def write_info_into_data_base(self, goods_list):
        if not os.path.exists(self.data_base_file_name):
            self._create()
        with sqlite3.connect(self.data_base_file_name) as con:
            cursor = con.cursor()
<<<<<<< HEAD
            for good in goods_list:         
                cursor.execute(""" INSERT INTO goods_info
=======
            for good in goods_list:
                if good['_price'] == '0' or good['_price'] == '':
                    print(f'Сайт не містить інформацію про товар з номером {good["item_id"]}')
                else:
                    print(f'Товар № {good["item_id"]} заноситься в базу даних')
                    cursor.execute(""" INSERT INTO goods_info
>>>>>>> 9c26894f9834a366849c6c12a7c14f32f9e7b3b6
                                    VALUES(?, ?, ?, ?, ?, ?, ?)""",
                                   (good['item_id'], good['_title'], int(good['_price']),
                                    int(good['_old_price']), good['_href'], good['_brand'],
                                    good['_category'])
                                   )
<<<<<<< HEAD
                con.commit()            
            
=======
                    con.commit()

>>>>>>> 9c26894f9834a366849c6c12a7c14f32f9e7b3b6

if __name__ == "__main__":
    csv1 = CsvOperation('test.csv')
    result = csv1.read_id_from_csv()
    db1 = DataBaseOperation('rozetka_goods.db')
    db1.write_info_into_data_base(result)
 