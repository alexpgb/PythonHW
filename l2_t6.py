import os
prod = []
pd = ['название', 'цена', 'количество', 'ед.изм']
pcount = []
pnmax = -1
a = {}
while True:
    os.system('cls')
    pl = []
    v = input('Введите номер товара (q-выход, n-новый товар) : ')
    if v == 'q':
        break
    elif v == 'n':
       pnmax = pnmax + 1
       v = pnmax
       prod.append((v, {}))
    elif not v.isdigit():
        print(f'Нужно число', end=''); v = input(f'Нажмите Enter для продолжения')
        continue
    v = int (v)
    if v < 0 or v > pnmax:
        print(f'Товара с таким номером нет', end=''); v = input(f'Нажмите Enter для продолжения')
        continue
    for pdk in pd:
        v1 = input(f'Для товара № {v} укажите {pdk} : ')
        prod[v][1][pdk] = v1
    print(f'Результат - {prod[v]}')
if len(prod) > 0:
    print(f'Результат prod - {prod}')
    for el in pd:
        l = []
        for i in range(pnmax + 1):
            l.append(prod[i][1][el])
        l = list(set(l))
        a[el] = l
        print(a[el])
    print(f'Результат a - {a}')
else:
    print('Bye...')