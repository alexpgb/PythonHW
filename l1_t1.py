v1_int = 2
v2_string = 'Это строка'
v3_float = 3.14
v4_bool = False
v4_list = [v1_int, v2_string, v3_float, v4_bool]
v5_turple = (v1_int, v2_string, v3_float, v4_bool)
v6_dict = {"v1_int": v1_int, "v2_string": v2_string, "V3_float": v3_float, "v4_list": v4_list, "v5_turple": v5_turple}

v7_ask_int = int(input("Жду целое число: "))
v8_ask_float = float(input("Жду нецелое число: "))
v9_ask_string_1 = input("А теперь жду мысль: ")
v10_ask_string_2 = input("А теперь еще одна мысль: ")
v_result = "Одна голова хорошо, а две лучше"

print("Это целое число", v1_int)
print("Это значение переменой типа float %.3f" % v3_float)
print("Это значение переменой типа bool {}".format(v4_bool))
print(f"Это значение переменной типа строка: {v2_string}")
print("Это значение переменной типа список:", v4_list)
print(f"Это значение переменной типа список через f строку:{v4_list}")
print(f"Это значение переменной типа turple через f строку:{v5_turple}")
print(f"Это первый элемент переменной типа turple через f строку:{v5_turple[1]}.\nЭто второй элемент :{v5_turple[1]}")
print(f"Это значение переменной типа словарь\n {v6_dict}")
print(f"Сумма целого и нецелого числа равна: {v7_ask_int+v8_ask_float}")
print(f"Сумма нецелого числа и строки: {str(v8_ask_float)+' '+v2_string}")
print(f"Сумма двух строк: {v2_string+'Это еще одна строка'}")
print(f"Если первая мысль-{v9_ask_string_1} + вторая мысль - {v10_ask_string_2} = {v_result}")

