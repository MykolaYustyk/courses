'''
2. Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків
2. fill() - заповнить створений масив числами - по порядку. Наприклад:
+────+────+
| 1  | 2  |
+────+────+
| 3  | 4  |
+────+────+
| 5  | 6  |
+────+────+
3. print_out() - виведе створений масив (якщо він ще не заповнений даними - вивести нулі
4. transpose() - перевертає створений масив. Тобто, якщо взяти попередню таблицю, результат буде
+────+────+────+
| 1  | 3  | 5  |
+────+────+────+
| 2  | 4  | 6  |
+────+────+────+
'''

class Matrix:
    
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.array_of_matrix = [[0 for i in range(self.columns)] for j in range(self.rows)]
    
        
    def fill(self):
        i = 1
        for row in range(self.rows):
            for column in range(self.columns):
                self.array_of_matrix[row][column]= i
                i += 1
                
    
    def print_out(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.array_of_matrix[i][j], end=' ')
            print()
            
    def transpose(self):
        transpose_matrix = list(zip(*self.array_of_matrix))
        for i in range(self.columns):
            for j in range(self.rows):
                print(transpose_matrix[i][j], end=' ')
            print()


if __name__ == "__main__":   
    matrix1 = Matrix(3,2)
    print('Початкова матриця')
    matrix1.print_out()
    print('Заповнена матриця')
    matrix1.fill()
    matrix1.print_out()
    print('Транспонована матриця')
    matrix1.transpose()
