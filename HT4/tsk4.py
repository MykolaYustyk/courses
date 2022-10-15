'''
   Створіть ф-цiю, яка буде отримувати довільні рядки та  обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел та окремо рядок без цифр та знаків лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
'''

def work_until_30(word):
    result = ''
    sum_of_nums = 0
    for char in word:
        if char.isdigit():
            sum_of_nums += int(char)
        if char.isalpha():
            result += char
    print(f'Сума всіх чисел = {sum_of_nums} \n')
    print(f'Рядок без цифр та знаків: {result}')
    return

def work_30_50(word):
    count_of_digits = 0
    count_of_letters = 0
    print(f'Довжина рядка дорівнює {len(word)}')
    for char in word:
        if char.isdigit():
            count_of_digits += 1
        if char.isalpha():
            count_of_letters += 1
    print(f'Кількіст цифр: {count_of_digits}')
    print(f'Кількість літер: {count_of_letters}')
    return

def work_above_50(word):
    ''' Функція видаляє голосні літери i '''
    result = [letter for letter in word if letter not in 'aoiueAOIUEуеіаояиюУЕІАОЯИЮ' and letter.isalnum()]
    result = ''.join(result)
    