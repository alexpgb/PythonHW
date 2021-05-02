# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class MyEx(Exception):
    def __init__(self, t):
        self.t = t


class Warehouse:
    """
    prod - товарные позиции;
    owner - владелец склада;
    storekeeper - кладовщик;
    address - адресс;
    capacity - вместимость;
    is_work - работает склад или нет.
    """
    def __init__(self, o, c, a):
        self.prod = {}
        self.owner = o
        self.storekeeper = ''
        self.address = a
        self.capacity_max = c
        self.is_work = 0
        self.capacity = 0

    def open(self, s):
        self.storekeeper = s
        self.is_work = 1

    def receipt(self, p, q):
        """
        Приход товара на склад
        p - товар - объект
        q - Количество
        """
        err_msg = []
        if type(q) != int: err_msg.append('Количество может быть только целым числом.') ; q=1
        if int(q) <= 0: err_msg.append('Количество должно быть положительным.')
        if self.is_work == 0: err_msg.append('Склад закрыт.')
        if self.capacity + p.package_size * q > self.capacity_max: err_msg.append('Склад переполнен.')
        if len(err_msg) > 0: raise MyEx(err_msg)
        if p.sku in self.prod.keys():
            self.prod[p.sku][0] = self.prod[p.sku][0] + q
        else:
            self.prod[p.sku] = [q, p]
        self.capacity = self.capacity + p.package_size * q
        print(f'Оприходован {p.model} остаток места на складе {self.capacity_max - self.capacity}')

    def release(self, p, q):
        if type(q) != int: raise MyEx('Количество может быть только целым числом.')
        if int(q) <= 0: raise MyEx('Количество должно быть положительным.')
        if self.is_work == 0 : raise MyEx('Склад закрыт')
        if p.sku not in self.prod.keys(): raise MyEx(f'Товара {p.model} нет на складе.')
        if self.prod[p.sku][0] < q: raise MyEx(f'Товара {p.model} недостаточно на складе.')
        self.prod[p.sku][0] = self.prod[p.sku][0] - q
        self.capacity = self.capacity - p.package_size * q
        print(f'Списан {p.model} остаток места на складе {self.capacity_max - self.capacity}')


class OfEq:
    def __init__(self, sku, m, p, s):
        self.sku = sku
        self.model = m
        self.price = p
        self.package_size = s


class Printer(OfEq):
    d_types = ['Matrix', 'Laser', 'Inkjet']

    def __init__(self, sku, m, p, s, t, nc):
        super().__init__(sku, m, p, s)
        if t not in self.d_types: raise MyEx(f'Несуществующий тип принтера {t}')
        self.name = 'Printer'
        self.d_types = t
        self.num_of_copy = nc   # ресурс


class Scanner(OfEq):
    d_types = ['Tablet', 'Extension']

    def __init__(self, sku, m, p, s, t):
        super().__init__(sku, m, p, s)
        if t not in self.d_types: raise MyEx('Несуществующий тип сканера')
        self.name = 'Scanner'
        self.d_types = t


class Copier(OfEq):
    d_types = ['Laser', 'Risograph']

    def __init__(self, sku, m, p, s, t):
        super().__init__(sku, m, p, s)
        if t not in self.d_types: raise MyEx('Несуществующий тип копира')
        self.name = 'Copier'
        self.d_types = t


w = Warehouse('ООО Быстрый чижик', 45,'Пролетная 15')
p1 = Printer('p12554', 'Laser Jet 1715', 25000, 5, 'Laser', 3000)
p2 = Printer('p12587', 'Ink Jet 457', 15000, 3, 'Inkjet', 3000)
s1 = Scanner('s25258', 'Canon Fast scan', 9500, 2, 'Tablet')
c1 = Copier('c12548', 'Epson', 90000, 15, 'Risograph')
c2 = Copier('c12448', 'Xerox', 80000, 12, 'Laser')
w.open('Тетя Дуся Сковородкина')
w.receipt(p1, 3)
w.receipt(p2, 2)
w.receipt(s1, 5)
w.release(p1, 3)
w.receipt(c1, 1)
# w.release(c2, 1) # списание несуществующего товара - сопровождается исключением.
s = '\n'.join([f'Товар {i} количество {w.prod[i][0]}' for i in w.prod.keys() if w.prod[i][0] > 0])
print(s)
