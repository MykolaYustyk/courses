'''
   Створіть ф-цiю, яка буде отримувати довільні рядки на зразок цього та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
'''
def work_30_50(word):
    count_of_digit = 0
    count_of_chars = 0
    for char in word:
        if char.isdigit():
           count_of_digit += 1
        if char.isalpha():
            count_of_chars += 1
            
    print(f'Довжина рядку: {len(word)}')
    print(f'Кількість цифр: {count_of_digit}')
    print(f'Кількість літер: {count_of_chars}')
    return
 
def work_until_30(word):
    sum_of_digit = 0
    word_without_digits = ''.join(char for char in word if char.isdigit())
    for char in word:
       if char.isdigit():
          sum_of_digit += int(char)
    print(f'Сума цифр в рядку: {sum_of_digit}')
    print(f'Рядок без цифр: {word_without_digits}')
    return

def phantasy(word):
    ''' Фукція видаляє голосні літери '''
    return''.join(char for char in word if char not in 'euioaEUIOAуеіаоєяиюїУЕЇІАОЄЯИЮ')
 
input_word = input('Введіть рядок:\n' )
if len(input_word) < 30:
   work_until_30(input_word)
elif 30 <= len(input_word) <= 50:
   work_30_50(input_word)
elif len(input_word) > 50:
   print(f'Новий рядок: {phantasy(input_word)}') 