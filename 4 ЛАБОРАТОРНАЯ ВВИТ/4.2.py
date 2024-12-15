import my_module
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
result = my_module.sum_numbers(a, b)

print(f"Сумма {a} и {b} равна: {result}")