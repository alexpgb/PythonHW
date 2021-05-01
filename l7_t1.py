# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from random import randint


class Matrix:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.m = [[None for _ in range(self.j)] for _ in range(self.i)]

    def set_rand(self, mn, mx):
        self.m = [[randint(mn, mx) for _ in range(self.j)] for _ in range(self.i)]

    def __add__(self, other):
        # print(self.m)
        # print(other.m)
        mr = Matrix(self.i, self.j)
        for i in range(self.i):
            for j in range(self.j):
                mr.m[i][j] = self.m[i][j] + other.m[i][j]
        return mr

    def __str__(self):
        return '\n'.join([''.join("{:>3d}".format(self.m[i][j]) for j in range(len(self.m[i]))) for i in range(len(self.m))])


mx = 3
my = 3
m1 = Matrix(my, mx)
m2 = Matrix(my, mx)
m1.set_rand(0, 10); m2.set_rand(0, 5)
# m3 = [[randint(0, 5) for _ in range(mx)] for _ in range(my)]
# print(m3[1])
# s1 = map("{:>3d}".format(), m3[1])
# s = '\n'.join([''.join("{:>3d}".format(m3[i][j]) for j in range(len(m3[i]))) for i in range(len(m3))])
# print(s)
print(m1)
print(m2)
ms = m1 + m2
# print(len(m1))
print(ms)
# print(len(ms))
