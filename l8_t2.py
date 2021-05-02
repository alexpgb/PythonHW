# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class MyExZeroDiv(Exception):
    def __init__(self, t):
        self.t = t


def main():
    res = 0
    v = list(map(float, input(f'Введите делимое и делитель, разделенные пробелом : ').split()))
    try:
        if v[1] == 0:
            raise MyExZeroDiv('Делить на ноль нельзя')
        else:
            res = v[0]/v[1]
    except MyExZeroDiv as mzde:
        print(mzde)
    return res

print(main())
