
class Cell:
    def __init__(self, c):
        if c <= 0:
            raise Exception('Количество клеток должно быть больше нуля')
        self.c = c

    def __add__(self, other):
        return Cell(self.c + other.c)

    def __sub__(self, other):
        if self.c > other.c:
            return Cell(self.c - other.c)
        else:
            print (f'Вычитание невозможно')
    def __mul__(self, other):
        return Cell(self.c * other.c)

    def __truediv__(self, other):
        return Cell(self.c // other.c)

    def __str__(self):
        return '*' * self.c

    def make_order(self, n):
        return ("*".__mul__(n)+"\n").__mul__(self.c//n) + "*" * (self.c % n)

c1 = Cell(9)
c2 = Cell(5)
c3 = c1 + c2
print(f' сумма:\n{c3.make_order(4)}')
c3 = c1 - c2
print(f' вычитание:\n{c3.make_order(4)}')
c3 = c1 * c2
print(f' произведение:\n{c3.make_order(10)}')
c3 = c1 / c2
print(f' деление:\n{c3.make_order(10)}')
