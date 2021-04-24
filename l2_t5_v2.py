#l = [9, 7, 6, 5, 4, 2]
#i = 5
#print(min(l, key=l-i))
l = [9, 7, 6, 5, 4, 2]
while True:
    v = input('Введите число (q-выход): ')
    if v == 'q':
        break
    #print(l)
    v = int(v)
    x = 0
    lx = 0
    print(f' оригинальный список: {l}')
    i = -1
    while True:
        i = i + 1
        if l[i] < v:
            l.insert(i, v)
            break
        if i == len(l)-1:
            l.append(v)
            break
    print(l)
