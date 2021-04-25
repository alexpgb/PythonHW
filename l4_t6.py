from random import randrange
from itertools import count, cycle

# почему то в таком виде не работает
# def my_iter(a1):
#     for el in count(a1):
#         try:
#             if el > 5: break
#             yield el
#         except StopIteration:
#             print(f'my_iter - закончился ')


def my_iter(a1):
    for el in count(a1):
#       как остановаить итератор изнутри итератора корректно ошибка возникает не здесь, а при вызове next снаружи
        if el > 10: break
        yield el


def my_iter_c(li):
#   такая штука не работает т.к. функция вызвывается один раз, как остановить этот итератор изнутри итератора?
    global n
    n = n + 1
    print(f' n - {n}')
    for el in cycle(li):
        if n > 10: break
        yield el


n = 0
i = my_iter(3)
print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i));
print(next(i))
# print(next(i))

ls = [randrange(0, 3) for _ in range(5)]
print(ls)
i = my_iter_c(ls)
print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i)); print(next(i));
print(next(i))
print(next(i))
