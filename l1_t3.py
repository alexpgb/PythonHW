i = 1
while i != 0:
    i = int(input("Жду целое число от 1 до 9 (0-выход):"))
    if i == 0:
        print("Bye!")
    elif i < 0:
        print("Число меньше нуля")
    elif i > 9:
        print("Число больше 9")
    else:
        print("Вот вам результат:", (i//1*100+i//1*10+i//1))
