fc = []
s = 20
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
    t = f'Сотрудники с зарплатой менее {s} :'+", ".join([fc[i][0] for i in range(len(fc)) if float(fc[i][1]) < s])
    print(t)
#    print(f'Количество строк {len(fc)}', end='')
#   Подсмотрел решение в домашке, т.к. у самого не получилось приколхозить вывод содержимого файла в одной строке.
#    t = [f'\nВ строке № : {ln}. "{lc.replace(chr(10),"")}" - слов {str(len(lc.split()))}.' for ln, lc in enumerate(fc, 1)]
#    print(*t)
