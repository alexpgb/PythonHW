from random import randint
fn = input(f'Задайте имя файла без расширения (расширение по будет txt) : ')+'.txt'
if fn == '.txt': fn = 'test'+str(randint(1, 50))+'.txt'
fc = ' '.join([str(randint(0, 1000)) for _ in range(randint(10, 20))])
print(fc)
if len(fc) > 0:
    with open(fn, 'w') as f:
        f.write(fc)
    f.close()
    print(f'Файл {fn} записан')
    fc = 0
    with open(fn, 'r') as f:
        for fl in f:
            fc = fc + sum(list(map(float, fl.split())))
    f.close()
    print(f'Сумма чисел в файле {fn} равна {fc}')
