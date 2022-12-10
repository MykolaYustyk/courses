import csv
import sqlite3
import os.path


from rozetka_api import RozetkaAPI


class CsvOperation:
    
    def __init__(self, file_name):
        self.file_name = file_name


    def read_id_from_csv(self):
        result = []
        with open(self.file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=',', fieldnames=['id'])
            reader = list(reader)
            for row in reader[1:]:
                item_id = int(row['id'])
                current_item = RozetkaAPI(item_id)
                good = current_item.get_item_data()
                if good['price'] == 0:
                    print(f'Сайт не містить інформацію про товар з номером {good["item_id"]}')
                else:
                    print(f'Товар № {good["item_id"]} заноситься в базу даних')
                    result.append(current_item.get_item_data())
        return result

class DataBaseOperation:

    def __init__(self, data_base_file_name):
        self.data_base_file_name = data_base_file_name
        
    
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
            
            
    def write_info_into_data_base(self, goods_list):
        if not os.path.exists(self.data_base_file_name):
            self._create()
        with sqlite3.connect(self.data_base_file_name) as con:
            cursor = con.cursor()
            for good in goods_list:         
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
    db1.write_info_into_data_base(result)
 