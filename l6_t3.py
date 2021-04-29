# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# - Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# - Создать класс Position (должность) на базе класса Worker.
# - В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# - Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    __income = {"wage": 1, "bonus": 0.25}

    def __init__(self, n, s, p, i):
        self.name = n
        self.surname = s
        self.position = p
        self._income = dict([("wage", Worker.__income['wage'] * i), ("bonus", Worker.__income['bonus'] * i)])
        print(f' income + bonus d ', self._income)


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.position

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p1 = Position('Афанасий', 'Умников', 'старший дуралей', 100000)
p2 = Position('Никифор', 'Шарящий', 'младщий дуралей', 120000)
print(f' значения аттрибутов p1 {p1.name} {p1.surname} {p1.position}')
print(f' значения аттрибутов p2 {p2.name} {p2.surname} {p2.position}')
print(f' {p1.get_full_name()} зарплата : {p1.get_total_income()}')
print(f' {p2.get_full_name()} зарплата : {p2.get_total_income()}')

