'''
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
   з 2-ма числами, а саме додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атрибута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен повернути результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
'''
class Calc:
    
    last_result = None
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    
    def add(self):
       
        print(f'{self.first} + {self.second}')
        print(f'last_result --> {self.last_result}')
        Calc.last_result = self.first + self.second
    
    
    def minus(self):
        
        print(f'{self.first} - {self.second}')
        print(f'last_result --> {self.last_result}')
        Calc.last_result = self.first - self.second
        
        
    def multiply(self):
        
        print(f'{self.first} * {self.second}')
        print(f'last_result --> {self.last_result}')
        Calc.last_result = self.first * self.second
    
    
    def division(self):
        
        print(f'{self.first} / {self.second}')
        print(f'last_result --> {self.last_result}')
        Calc.last_result = self.first / self.second

if __name__ == '__main__':   
    nums1 = Calc(1, 1)
    print(f'last_result --> {nums1.last_result}')
    nums1.add()
    nums2 = Calc(2, 3)
    nums2.minus()
    nums3 = Calc(3, 4)
    nums3.multiply()
    nums4 = Calc(4, 5)
    nums4.division()