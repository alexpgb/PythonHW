# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplNum:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplNum(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplNum(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)

    def __str__(self):
        return f'{self.re} {"+" if self.im >= 0 else "-"} {abs(self.im)}i'


c1 = ComplNum(5, 2)
c2 = ComplNum(2, -5)
print(c1)
print(c2)
c3 = c1 + c2
c4 = c1 * c2
print(c3)
print(c4)
