from json import dump, dumps
fc = []
fn = 't7.txt'
rl = []
while True:
#    fn = input(f'Задайте имя файла с расширением ')
    if len(fn) == 0: break
    try:
        with open(fn, 'r') as f:
            f.close()
    except FileNotFoundError:
        print(f'Файл {fn} не существует.')
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        print(f'Файл {fn} открыт')
        for fl in f:
            if len(fl) > 0: fc.append(fl.split())
        f.close()
        print(f'Файл {fn} закрыт')
    break
print(fc)
d1 = {fc[i][0]: int(fc[i][-2])-int(fc[i][-1]) for i in range(len(fc))}
d2 = [d1.get(k) for n, k in enumerate(d1.keys())]
d2 = dict(average_profit=round(sum(d2)/len(d2), 2))
rl.append(d1)
rl.append(d2)
print(rl)
fn = fn.replace('.', '_new.')
with open(fn, 'w') as f:
    dump(rl, f)
f.close()
print(f'Файл {fn} записан')
