from functools import reduce


def comp(a, b):
    return a * b


G = (i for i in range(100, 1001, 2))
print(reduce(comp, G))
# или так
# print(reduce(comp, (i for i in range(100, 1001, 2))))


