s = ''
while True:
    s = input('Введите несколько слов или символов, разделенных пробелами (q - выход)')
    if len(s) > 0:
        if s == 'q':
            break
    else:
        print('Не может быть пустая строка')
        continue
    for i, el in enumerate(s.split()):
        print(f'Номер строки - {i+1} элемент - {el[:10]}')
