fc = []
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
            fc.append(fl)
        f.close()
        print(f'Файл {fn} закрыт')
    print(fc)
    print(f'Количество строк {len(fc)}', end='')
#   Подсмотрел решение в домашке, т.к. у самого не получилось приколхозить вывод содержимого файла в одной строке.
    t = [f'\nВ строке № : {ln}. "{lc.replace(chr(10),"")}" - слов {str(len(lc.split()))}.' for ln, lc in enumerate(fc, 1)]
    print(*t)
# так тоже не получилось.
#    print((a := [str(len(fc[i].split())) for i in range(len(fc))], '\n', [i for i in a]), sep='')
# почему то не получается сформировать строку через лямбда функцию.
#    F = (lambda x: "Количество  строк "+str(len(x[i].split())) for i in range(len(x)))
#    print(F(fc))
