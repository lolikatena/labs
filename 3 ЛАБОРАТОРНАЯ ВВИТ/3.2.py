def write_to_file(filename, text, mode = 'w'):
    with open(filename, mode) as file:
        file.write(text + '\n') #делаем текст с новой строки

user_input=input('Введите текст: ')
write_to_file('user_input.txt', user_input)
print('Текс успешно записан')

more_text = input('Введите добавочный текст: ')
write_to_file('user_input.txt', more_text, mode='a')
print('Текс добавлен!')