def user_info_print(last_name, first_name, bd_year, city, email, phone):
    print(f'Информация о пользователе: Имя - {last_name} , Фамилия - {first_name}, год рождения - {bd_year}, город проживания - {city} , Email - {email}, телеофн - {phone}')


def user_info_print1(**kwargs):
    print(f'Информация о пользователе: Имя - {kwargs["last_name"]} '
          f', Фамилия - {kwargs["first_name"]},'
          f' год рождения - {kwargs["bd_year"]},'
          f' город проживания - {kwargs["city"]} , Email - {kwargs["email"]}, телеофн - {["phone"]}')


user_info_print(last_name='Иван', first_name='Иванов', bd_year='2003', city='Верхняя Пышма', email='ivan_i@mail.ru', phone='79998887766')
user_info_print1(last_name='Иван', first_name='Иванов', bd_year='2003', city='Верхняя Пышма', email='ivan_i@mail.ru', phone='79998887766')
