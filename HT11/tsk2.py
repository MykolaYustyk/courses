'''
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати якісь аргументи,
   які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атрибут profession (його не має інсувати під час
  ініціалізації в самому класі) та виведіть його на екран (прінтоніть)
'''

class Person:
    ''' class of a person '''    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def show_age(self):
        '''method shows age of person'''
        return f'Age of person is {self.age}'
    
    
    def print_name(self):
        '''method prints person name'''
        print(f'Person name is {self.name}')
        
        
    def show_all_information(self):
        '''print all information about person'''
        return f'{self.name} is {self.age} old'
    

if __name__ == "__main__":  
    person_1 = Person('Tom', 30)
    person_2 = Person('Mary', 26)
    person_1.profession = 'driver'
    person_2.profession = 'nurse'
    print(person_1.show_age())
    print(person_2.print_name())
    print(person_1.show_all_information())
    print(person_2.show_all_information())
    print(person_1.profession)
    print(person_2.profession)  