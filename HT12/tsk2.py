'''
2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки (включіть фантазію). 
   Наприклад вона може містити класи Person, Teacher, Student, Book, Shelf, Author, Category і.т.д. Можна 
   робити по прикладу банкомату з меню, базою даних і т.д.
'''
import sqlite3
import datetime

start_menu_list = ['Читачі', 'Книжний фонд', 'Вихід']
reader_menu_list = ['Переглянути список читачів', 'Додати читача', 'Видалити читача', 'Формуляр читача', 'До головного меню']
book_menu_list = ['Переглянути інформацію про книгу', 'Додати нову книгу', 'Взяти книгу', 'Повернути книгу', 'До головного меню']

def my_decorator(function):
    def wrapper(*args, **kwargs):
        print()
        print('-' * 35)
        result = function(*args, **kwargs)
        print('-' * 35)
        return result
    return wrapper

class Person:       
    def __init__(self, name=''):
        self.name = name
   
              
class Reader(Person):  
    def __init__(self, name=''):
        super().__init__(name)
        
    @staticmethod
    @my_decorator
    def show_readers_list():
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM readers')
            for i, name in enumerate(cursor.fetchall(), 1):
                print(f'{i}. {name[0]}')
    
    @staticmethod
    def add_new_reader():
        while True:
            current_name = input('Введіть прізвище i im\'я читача: ')
            new_reader = Reader(current_name)  
            with sqlite3.connect('library.db') as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT * FROM readers WHERE name == ?',(current_name,))
                if cursor.fetchone() is None:
                    cursor.execute(f'INSERT INTO readers VALUES("{new_reader.name}")')
                    con.commit()
                    print(f'Читача {new_reader.name} успішно додано')
                    break
                else:
                    print('Такий читач вже зареєстрований.')
                    print('Повторіть ввод')
            return 
        
        
    def remove(self):
        current_name = self.name
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'DELETE FROM readers WHERE name = "{current_name}"')
            con.commit()                
        
        
class Author(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def write_the_books(self):
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            
               
        
class Book(Author):
    count = 0
    
    def __init__(self, name='', title='', publish_year=0,avail=1):
        super().__init__(name)
        self.title = title
        self.publish_year = publish_year 
        self.avail = avail       
        self.__class__.count = self.add_count()
        

    @classmethod
    def add_count(cls):
        cls.count += 1
        return cls.count
    
    @classmethod
    def change_avail(self):
        if self.avail:
            self.avail = False
        else:
            self.avail = True
        return self.avail
        
    @my_decorator
    def show_information(self):
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM books WHERE title = ?', (self.title,))
            current_book = cursor.fetchone()
            print(  f'Інформація про книгу \n'
                    f'{"-" * 35}\n'
                    f'Автор: {current_book[0]}\n'
                    f'Назва: {current_book[1]}\n'
                    f'Рік видання: {current_book[2]}\n'
                    f'Наявність: {current_book[3]}'
                )
            
    
    def add_new_book(self):
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'INSERT INTO books VALUES(?, ?, ?, ?)', (self.name, self.title, self.publish_year,self.avail))
            con.commit()
        print('Нову книгу додано')   
        
        
    def get_book(self):
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'UPDATE books SET avail = ? WHERE title =?', (0, self.title))
            con.commit()
        print(f'Книгу {self.title} взято')    
            

    def return_book(self):
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'UPDATE books SET avail = ? WHERE title = ?', (1, self.title))
            con.commit()
        print(f'Книгу {self.title} повернули')        
        
             
class Menu:

    def __init__(self, list_menu):
        self.list_menu = list_menu
        

    @my_decorator
    def show(self):
        for i, val in enumerate(self.list_menu, 1):
            print(f'{i}. {val}')
            

    def get_choice(self):
        while True:
            current_choice = input('Ваш вибір: ')
            if current_choice.isdigit() and 1 <= int(current_choice) <= len(self.list_menu):
                break
            else:
                print(f'Вибір повинен бути в межах від 1 до {len(self.list_menu)}')
                print('Повторіть ввод.')
        return int(current_choice)


start_menu = Menu(start_menu_list)
reader_menu = Menu(reader_menu_list)
book_menu = Menu(book_menu_list)

def get_name():
    while True:
        current_name = input('Введіть прізвище i im\'я: ')          
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM readers WHERE name = ?', (current_name,))
            if cursor.fetchone() is None:
                print("Читача з такими даними в базі даних немає ")
                print('Повторіть ввод')
            else:
                break
    return current_name   
        

def get_title():
    while True:
        current_title = input('Введіть назву книги: ')
        with sqlite3.connect('library.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM books WHERE title = ?', (current_title,))
            result = cursor.fetchone()
            if result[1] == current_title:
                result = Book(*result)      
                break
            else:
                print('Книжки з такою назвою не знайдено')
                print('Повторіть ввод')
    return result
        
  
def get_new_book():
    print('Додаєм нову книгу')
    new_book_author = input("Введіть прізвище і ім'я автора: ")
    new_book_title = input('Введіть назву книжки: ')
    new_book_publish_year = input('Рік видання:')
    new_book = Book(new_book_author, new_book_title, new_book_publish_year, 1)
    return new_book
    
   
def reader_routine():
    while True:
        reader_menu.show()
        choice = reader_menu.get_choice()        
        if choice == 1:
            reader = Reader()            
            reader.show_readers_list()
        elif choice == 2:
            reader = Reader()
            reader.add_new_reader()
        elif choice == 3:
            reader = Reader(get_name())
            reader.remove()
        elif choice == 4:
            reader = Reader(get_name())
            reader.show_books_history()
        elif choice == 5:
            break
            

def books_routine():
    while True:
        book_menu.show()
        choice = book_menu.get_choice()
        if choice == 1:
            book = get_title()
            book.show_information()
        elif choice == 2:
            book = get_new_book()
            book.add_new_book()
        elif choice == 3:
            book = get_title()
            book.get_book()
        elif choice == 4:
            book = get_title()
            book.return_book()
        elif choice == 5:
            break                 
            
    
def start():
    while True:
        start_menu.show()
        choice = start_menu.get_choice()
        if choice == 1:
            reader_routine()
        elif choice == 2:
            books_routine()
        elif choice == 3:
            break

   
if __name__ == "__main__":
    start()
print('Програма закінчила свою роботу. ')