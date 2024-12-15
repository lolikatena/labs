import random
def greet(name):
    grt = [f'Здравствуйте, {name}!',
        f'Добрый день, {name}!',
        f'Рады Вас видеть, {name}!',
        f'Ваззап {name}!!',
        f'Привет, {name}']
    random_grt = random.choice(grt)
    print(random_grt)

name = input('Введите Ваше имя: ')
greet(name)