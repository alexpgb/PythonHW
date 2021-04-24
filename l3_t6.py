def int_func1(a1):
    return a1.title() if len(a1) > 0 else None


def int_func2(a1):
    return a1[0].upper()+a1[1:] if len(a1) > 0 else None


while True:
    s = input(f'Введите слова разделенные пробелами (0 - выход) : ').split()
    if s == 'q':
        break
    else:
        print(' '.join(list(map(int_func1, s))))
        print(' '.join(list(map(int_func2, s))))
