def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print('Числа равны')
        return x

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
res = max_of_two(x,y)
print(f'Большее число: {res}')