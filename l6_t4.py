# 4. Реализуйте базовый класс Car.
# - У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# - А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# - Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# - Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# - Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# - Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    possible_d = ('Вперед', 'Назад', 'Вправо', 'Влево')

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.is_police = False
        self.d = None
        self.speed = 0

    def go(self, *args):
        """arg1 - speed, arg2 - direction """
        arg = list(args)
        if len(arg) == 1:
            arg.append(self.d)
        if not (arg[1] in Car.possible_d):
            print(f'Направление задано неправильно')
        if arg[0] < 0:
            if arg[1] == Car.possible_d[0]: self.d = Car.possible_d[1]
            if arg[1] == Car.possible_d[1]: self.d = Car.possible_d[0]
            self.speed = abs(arg[0])
        else:
            self.d = arg[1]
            self.speed = arg[0]
        print(f'Направление {self.d}. Скорость {self.speed}')

    def turn(self, direction):
        if not (direction in Car.possible_d):
            print(f'Направление задано неправильно')
        self.d = direction
        print(f'Повернули {self.d}. Скорость {self.speed}')

    def stop(self):
        self.speed = 0

    def show_speed(self):
        print(f'Направление {self.d}. Скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Направление {self.d}. Скорость {self.speed}')
        if self.speed > 60:
            print(f'Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Двигаемся {self.d}. Скорость {self.speed}')
        if self.speed > 40:
            print(f'Превышение скорости')


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


c1 = Car('Белый', 'Калина')
c2 = Car('Красный', 'Веста')
tc = TownCar('Синенький', 'Gets')
sc = SportCar('Черные глаза', 'Приора посаженая')
wc = WorkCar('Рыжий', 'Камаз')
pc = PoliceCar('Белосиний', 'Форд')
c1.go(80, 'Вперед')
c1.go(10)
c1.go(0)
c1.go(-3)
c1.turn('Влево')
c1.go(90, 'Вперед')
c2.go(-30, 'Назад')
c2.stop()
print(c2.is_police)
tc.go(120, 'Вперед')
wc.go(100, 'Вперед')
pc.go(100, 'Вперед')
print(pc.is_police)



