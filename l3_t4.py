def my_func1(a1, a2):
    return a1**a2


def my_func2(a1, a2):
    r = a1
    for i in range(1, abs(a2)):
#       print(range(1, abs(a2)))
        r = r * a1
#       print(r)
    return 1/r


while True:
    v1 = input('Введите два числа через пробел,\n 1 - основание степени-положительное число'
               '\n 2-показатель степени - целое отрицательное число'
               '\n  (q-exit) : ').split()
    if 'q' in v1:
        break
    elif not v1[0].isdigit or not v1[1].isdigit:
        print(f'Должны быть числа')
    elif float(v1[0]) <=0:
        print(f'Первое число должно быть больше нуля')
    elif int(v1[1]) >= 0:
        print(f'Второе число должно быть отрицательным')
    elif not float(v1[1]).is_integer():
        print(f'Второе число должно быть целым')
    else:
        print(my_func1(float(v1[0]), int(v1[1])))
        print(my_func2(float(v1[0]), int(v1[1])))

