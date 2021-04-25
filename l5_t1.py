from random import randint
fn = input(f'Задайте имя файла без расширения (расширение по будет txt) : ')+'.txt'
if fn == '.txt': fn = 'test'+str(randint(1, 50))+'.txt'
print(f'Построчно введите содержимое файла {fn}')
ln = 0
fc = []
while True:
    ln += 1
    fl = input(f'Cтрока {ln} : ')
#    print(fl, len(fl))
    if len(fl) == 0: break
    fc.append(fl+'\n')
if len(fc) > 0:
    with open(fn, 'w') as f:
        for fl in fc:
            f.write(fl)
    f.close()
    print(f'Файл {fn} записан')


