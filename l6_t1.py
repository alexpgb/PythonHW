# Создать класс TrafficLight (светофор).
#  определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# © geekbrains.ru 18
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.
from time import sleep
from itertools import cycle

# вынужден здесь определить переменную типа массив, потому что без нее не работает!!!
# почему то, если у меня здесь, за пределами класса нет определения словаря, то не инициализируетяся генератор
# внутри класса.
dtc = {1: {'color': 'Red', 'd': 7}, 2: {'color': 'Yellow', 'd': 2},
       3: {'color': 'Green', 'd': 5}, 4: {'color': 'Бледно розовый', 'd': 3}}


class TrafficLight:
    dtc_ = {1: {'color': 'Red', 'd': 7}, 2: {'color': 'Yellow', 'd': 2},
              3: {'color': 'Green', 'd': 5}, 4: {'color': 'Бледно розовый', 'd': 3}}
#    Пояснения к странной ситуации:
#    специально два идентичных словаря обозначены разными именами
    dtck = dtc_.keys()      # вот тут я легко обращаюсь к переменной dtc_
    dtcс = dtc_.get(1).get("color")  # вот тут я легко извлекаю значение по ключу из dtc_
#    а если я делаю так как в следующей строке порграмма падает с ошибкой потому, что не находит переменную dtc_
#    cl = [dtc_.get(i).get("color") for i in dtc_.keys()]
#    а вот так будет уже работать dtc.get(i).get("color") - берет из переменной модуля, а dtc_.keys() - нормально из
#    переменной внутри класса, почему так происходит? Надеюсь, что вы подскажете.
#    если я использую список вместо словаря, то на это месте программа тоже падает с тем же сообщением.
    cl = [dtc.get(i).get("color") for i in dtc_.keys()]
    cg = (i for i in cycle(cl))     # понимаю, что на уровне класса это делать не правильно,
    # потому, что генератор cg будет один на все экземпляры класа )

    #    а если я делаю self.dtc_ тоже не работает (и не должно), если делаю TrafficLight.dtc_ тоже не работает.

    __color = next(cg)
    color_next = next(cg)
    color_init = 'Black'

    def running(self, c):
        # Это просто эксперимент. Здесь мы проверяем, как изменяются аттрибуты класса и экземпляра класса.
        # print(f' type(TrafficLight.__color ', type(TrafficLight.__color))
        # print(f' type(self.__color ', type(self.__color))
        # self.color_prev = TrafficLight.__color
        # self.color_prev = self.__color
        # print(f'self.color_init до - {self.color_init}')
        # self.color_init = 'Grey'
        # print(f'self.color_init после - {self.color_init}')
        # print(f'TrafficLight до - {TrafficLight.color_init}')
        # TrafficLight.color_init = 'Grey'
        # print(f'TrafficLight после - {TrafficLight.color_init}')
        d = [self.dtc_.get(k).get('d') for k in self.dtc_.keys() if self.dtc_.get(k).get("color") == c]
        print(f' d - {d}')
#        если нам ввернули не пустой набор.
        if len(d) > 0:
            if c == self.__color:
                print(f'На светофоре {self.__color}')
                sleep(d[0])
                self.__color = self.color_next
                self.color_next = next(self.cg)
            else:
                print(f'Ожидаем цвет {self.__color}.')
        else:
            print(f'Такого цвета не предусмотрено.')

    def running_in_cycle(self):
        for i in self.dtc_.keys():
            self.__color = self.dtc_.get(i).get("color")
            print(f'На светофоре {self.__color}')
            sleep(self.dtc_.get(i).get('d'))


# print(TrafficLight.dtc_)
# print(dtc.keys())
# print(TrafficLight.dtck)
# print(TrafficLight.dtcс)

tl = TrafficLight()
tl.running('Red')
# print(f'tl.color_next ', tl.color_next)
# print(f'TrafficLight.color_next ', TrafficLight.color_next)
tl.running('Re')
# print(f'tl.color_next ', tl.color_next)
# print(f'TrafficLight.color_next ', TrafficLight.color_next)
tl.running('Red')
# print(f'tl.color_next ', tl.color_next)
# print(f'TrafficLight.color_next ', TrafficLight.color_next)
tl.running('Yellow')
tl.running('Green')
tl.running('Бледно розовый')
tl.running('Red')
tl.running_in_cycle()