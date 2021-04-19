time_in_sec = -1
while time_in_sec < 0:
    time_in_sec = int(input("Введите время в секундах:"))
    if time_in_sec < 0:
        print(f"Число меньше 0")
time_in_sec = int(time_in_sec)
print(f"{((time_in_sec%(3600*24))//3600):02}:{(time_in_sec%3600)//60:02}:{time_in_sec%60:02}")
