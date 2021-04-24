i = 0
l = []
while True:
    i = i + 1
    el = input(f'Нужен {i} элемент списка (/q-exit, /w-обработка): ')
    if el in ('/q', '/w'):
        if el == '/q' and 'y' == input('Точно выходим? Если да, нажмите y '):
            break
        else:
            break
    else:
        l.append(el)
if el == '/w':
    print(l)
    for i in range(len(l)//2):
        f = i * 2
        s =  i * 2 + 1
        # print(i, l[i*2], l[i*2+1], l[i*2], l[i*2+1])
        # странно, что вот в таком виде обмен значениями не работает почему то?
        #l[(i * 2)], l[(i * 2 + 1)] = l[(i * 2)], l[(i * 2 + 1)]
        # присваивание работает, а обмен нет
        #l[(i * 2)] = l[(i * 2 + 1)]
        # print(i, l[f], l[s], l[s], l[f])
        l[f], l[s] = l[s], l[f]
        print(l)
    print(l)
else:
    print(f'Bye...')
