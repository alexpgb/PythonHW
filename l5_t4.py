d = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
fc = []
fn_new = 't4_new.txt'
while True:
    fn = input(f'Задайте имя файла с расширением ')
    if len(fn) == 0: break
    try:
        with open(fn, 'r') as f:
            f.close()
    except FileNotFoundError:
        print(f'Файл {fn} не существует.')
        continue
    with open(fn, 'r') as f:
        print(f'Файл {fn} открыт')
        for fl in f:
            fc.append(fl.split())
        f.close()
        print(f'Файл {fn} закрыт')
    print(fc)
    fcn = '\n'.join([' '.join([d.get(fc[i][0]), fc[i][1], fc[i][2]]) for i in range(len(fc))])
    print(fcn)
    fn = fn.replace('.', '_new.')
    with open(fn, 'w') as f:
        f.write(fcn)
    f.close()
    print(f'Файл {fn} записан')

