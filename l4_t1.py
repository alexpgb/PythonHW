from sys import argv

print(f'Расчет заработной платы:\n'
      f'выработка - {int(argv[1])}\nставка - {float(argv[2])}\n'
      f'премия - {int(argv[3])}\nк выплате - {round(int(argv[1])*float(argv[2])+int(argv[3]),2)}')

# python l4_t1.py 10 1.5 20
# Расчет заработной платы:
# выработка - 10
# ставка - 1.5
# премия - 20
# к выплате - 35.0

# argv = 10
# rate = 1.5
# bonus = 20
# print(f'Расчет заработной платы:\n'
#       f'выработка - {prod}\nставка - {rate}\nпремия - {bonus}\nк выплате - {prod*rate+bonus}')