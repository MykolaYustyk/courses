'''
1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white
   і метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи _init_ для 
   завдання початкових розмірів об'єктів при їх створенні.
'''

class Figure:
    color = 'white'
    
    def __init__(self):
        pass
    
    
    @classmethod
    def change_color(cls, color):
        cls.color = color
    
    
class Oval(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Square(Figure):
    def __init__(self, side):
        self.side = side
        
if __name__ == "__main__":
    oval = Oval(3, 5)
    oval.change_color('red')
    print(f'Колір овалу {oval.color}')
    square = Square(10)
    square.change_color('yellow')
    print(f'Колір квадрату {square.color}')
    