from my_package.numbers import operations
from my_package.strings import manipulations
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
result_sum = operations.sum_numbers(a,b)
print(f"Сумма {a} и {b} равна: {result_sum}")
result_sub = operations.sub_numbers(a, b)
print(f"Разность {a} и {b} равна: {result_sub}")

result_reverse = manipulations.reverse_string(input('Введите текст: '))
print(f"Перевернутая строка : {result_reverse}")

result_upper = manipulations.upper_case(input('Введите текст: '))
print(f"Строка в верхнем регистре: {result_upper}")
