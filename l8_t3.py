# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.
from itertools import count


class MyExElNotNum(Exception):
    def __init__(self, t):
        self.t = t


def main():
    res = []
    for i in count(1):
        v = input(f'Введите {i} элемент списка  (stop - выход) : ')
        if v == 'stop':
            break
        try:
            if not v.isdigit():
                raise MyExElNotNum('Введенный параметр на число.')
        except MyExElNotNum as mex:
            print(mex)
        else:
            res.append(float(v))
        print(res)
    return res


print(main())
