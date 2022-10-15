'''
4. Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване значення
   (латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensitive (на ваш розсуд - великими чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть. Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..- -...   .. ...   .... . .-. .
    результат: GEEKHUB IS HERE
'''


import string


def morse_decoder(morse_message):
    list_of_letters = list(string.ascii_uppercase) +['SOS']
    list_of_sign = ['.-', '-...', '-.-.', ' -..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '...---...']
    dict_result = {sign: letter for sign, letter in zip(list_of_sign, list_of_letters)}
    
    print(f'Input Morze massage is: {morse_message}')
    morse_string = morse_message.strip().split('   ')
    morse_letters  = [word.split(' ') for word in morse_string]
    morse_letters = [[dict_result.get(sign, '*') for sign in word] for word in morse_letters]

    result = ' '.join(''.join(word) for word in morse_letters)
    return f'Output message is: {result}'
    
    
morse_message = '--. . . -.- .... ..- -...   .. ...   .... . .-. .'
print(morse_decoder(morse_message))