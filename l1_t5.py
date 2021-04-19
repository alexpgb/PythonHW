i = '0'
rev = 0
exp = 0
staff = 0
while True:
    i = input("Какая выручка (q-выход):")
    if i == 'q':
        print("Bye!")
        break
    else:
        rev = int(i)
        exp = int(input("А расходы:"))
        if rev > exp:
            staff = int(input("Напомните, сколько у вас сотрудников :"))
            if staff > 0:
                print(f"Поздравляем, у вас прибыль {rev-exp}!\nРентабельность {(rev-exp)/rev:.0%}.\nПрибыль на сотрудника {(rev-exp)/staff:.2f}.")
        elif rev < exp:
            print(f"Оу, да у вас убытки {rev-exp}!")
        elif rev == exp:
            print(f"Увы и ах, получился {rev-exp}...")
        else:
            print(f"Да у вас там черт ногу сломит в бухгалтерии!")
