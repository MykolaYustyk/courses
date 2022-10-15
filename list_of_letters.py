import string

list_of_letters = list(string.ascii_uppercase) +['SOS']
list_of_sign = ['.-', '-...', '-.-.', ' -..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '...---...']
dict_result = {sign: letter for sign, letter in zip(list_of_sign, list_of_letters)}

morse_string = input('Input Morze code: ').strip().split('   ')
morse_letters  = [word.split(' ') for word in morse_string]
morse_letters = [[dict_result.get(sign, '*') for sign in word] for word in morse_letters]

result = ' '.join(''.join(word) for word in morse_letters)
print(f'Result: {result}')
