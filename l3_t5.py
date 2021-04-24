q = 0
r = 0
while True:
    v1 = input(f'Промежуточный результат : {r} \n'
               f'Введите числа в строку, разделенные пробелами (q-exit): ').split()
    if 'q' in v1:
        v1 = v1[:v1.index('q')]
        q = 1
    r = r + sum(list(map(lambda x: int(x) if float(x).is_integer() else float(x), v1)))
    if q == 1: break
print(f'Сумма чисел : {r}')