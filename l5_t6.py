d = {}
fc = []
fn = 't6.txt'
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
            fc.append(fl.split())
        f.close()
        print(f'Файл {fn} закрыт')
    break
print(fc)
d1 = {fc[i][0][:(fc[i][0].find(':'))]:2 for i in range(len(fc))}
i = 0
sm = 0
s = ''
print(len(fc))
for i in range(len(fc)):
    sm = 0
    dkey = fc[i][0][:(fc[i][0].find(':'))]
    s = ' '.join(fc[i])
    s = s.replace(dkey+':', '')
    s = s.replace('—', '')
    print(s)
    for j in range(s.count('(')):
        sm = sm + int(s[s.find(' ')+1: s.find('(')])
        s = s[s.find('(')+1:]
    d[dkey] = sm
print(d)
