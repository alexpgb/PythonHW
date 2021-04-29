# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Это {self.title}. Запуск отрисовки.')


class Pencil(Stationery):

    def draw(self):
        print(f'Это {self.title}. Запуск отрисовки.')


class Handle(Stationery):

    def draw(self):
        print(f'Это {self.title}. Запуск отрисовки.')


s1 = Pen('Ручка')
s2 = Pencil('Карандаш')
s3 = Handle('Маркер')

s1.draw()
s2.draw()
s3.draw()