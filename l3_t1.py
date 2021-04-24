def f_div(arg1, arg2):
    if arg2 == 0:
        print(f'Zero division')
    else:
        return arg1/arg2

    
while True:
    v1 = input('Введите два числа через пробел (q-exit) : ').split()
    if 'q' in v1:
        break
    elif not v1[0].isdigit or not v1[1].isdigit:
        print(f'Expected numbers')
    else:
        print(f_div(int(v1[0]), int(v1[1])))
