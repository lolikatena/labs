def describe_person(name, age=30):
    print(f'Имя: {name}')
    print(f'Возраст {age} лет')

name = input('Введите имя: ')
describe_person(name)
