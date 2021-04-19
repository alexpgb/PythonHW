i = 1
result = 0
result_tmp = 0
c = 1
while i != 0:
    i = int(input("Жду целое число больше нуля (0-выход):"))
    if i == 0:
        print("Bye!")
    elif i < 0:
        print("Число меньше нуля")
    else:
        while c < 10:
            result_tmp = (i % (10 ** c))//(10 ** (c-1))
#             print(f"c-{c}, i {i} {result_tmp} {(i % (10 ** (c-1)))} {(10**(c-1))} result {result} остановка {(i // (10 ** c) == 0)}")
            if result_tmp > result:
                result = result_tmp
                if (result == 9) or (i // (10 ** c) == 0):
                    i = 0
                    break
            c = c + 1
        print(f"Вот вам результат: {result:.0f}")
