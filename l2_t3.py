m = 0
s1 = (12, 1, 2)
s2 = (3, 4, 5)
s3 = (6, 7, 8)
season = {1:'Зима', 2:'Весна', 3:'Лето',4:'Осень'}
while True:
    m = input('Укажите номер месяца (q-выход) ')
    if m.isdigit():
        m = int(m)
        if m in range(1, 13):
            if m in s1:
                s = 1
            elif m in s2:
                s = 2
            elif m in s2:
                s = 3
            else:
                s = 4
            print(f'Время года {season.get(s)} ')
        else:
            print('Нужно число от 1 до 12')
    else:
        if m == 'q':
            break
        print('Нужно ввести число')
