# сказать честно я не понял что нужно сделать начиная с места:
# функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо
# выводить только первые n чисел, начиная с 1! и до n!.
# и просто посмотрел разбор домашки.

from math import factorial
from itertools import count


def my_fact():
    for a in count(1):
        yield factorial(a)


F = my_fact()
i = 1
for result in F:
    if i > 10: break
    print(f'Факториал {i} = {result}')
    i += 1
