'''
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска програми на екран виводиться в лівій половині - 
   колір автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні кольори.
   Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах (пішоходам зелений
   тільки коли автомобілям червоний).
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
'''

import time

colors = {'Red': 'Green',
          'Yellow': 'Red',
          'Green': 'Red'
         }

def change_colors():
    for i in range(12):
        if 0 <= i < 4:
            color = 'Red'
        elif 4 <= i < 6 or 10 <= i < 12:
            color = 'Yellow'
        elif 6 <= i < 10:
            color = 'Green'
        print(color.ljust(8), colors[color].ljust(8))
        time.sleep(1)
    return
    
def work_process():
    while True:
        change_colors()
        
    
if __name__ == "__main__":
    work_process()
           