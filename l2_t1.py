l = ['Its', 'my', 1, 'list', 3.14, (1,2,5)]
i = 0
for i in range(len(l)):
   print(f'тип {i} элемента списка {type(l[i])}')
print(f'тип самого списка {type(l)}')