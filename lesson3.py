# name = input("name: ")
# age = int(input("age: "))
# bio = 'Добро пожаловать {}, вам уже {}, с днем рождения!'.format(name,age)
# print(bio)
# print(f'Добро пожаловать {name}, авм уже {age}, с днем рождения!')

# Срезы и индексы
# name  = 'erjan saliev'
#         # 01234567891011
# # Срезы
# print(name[6:12])
# print(name[6:])
# print(name[6::2])
# print(name[::-1]) # переворачиваем строку

# Условия if else
# Если человеку меньше 16 то мы говорим "пока рано", если ему от 16 до 18 мы говорим "готовься", 
# если ему от 18 до 40 то "идем служить", если ему от 40-60 то он "пенсионер", если ему от 60-100, 
# "ветеран", вы должны сделать защиту дурака, чтобы человек если вводит отрицательные числа, получал 
# ошибку, если числа больше 100, тоже ошибка
# and, or, operators сраавнения 

# age = int(input())
# if age >0 and age < 16:
#     print("Пока рано")
# elif age>= 16 and age < 18:
#     print('Готовься')
# elif age>= 18 and age < 40:
#     print('идем служить')
# elif age>= 40 and age < 60:
#     print("пенсионер")
# elif age>= 60 and age < 100:
#     print("ветеран")
# else:
#     print(' Error')

# age = int(input())
# if age % 2 == 0:
#     print("Chet")
# else:
#     print("Nechet")

# print(7%2)

# List - Списки - [] - любые типы данных - массив
# list - [45,56,'slov', [3,4,56], True]
        # dict - {key:value}

    # Неизменяемые - unmutable
        # str - '', "", """"""
        # bool - True, False 
        # int - 445
        # float - 1.5
        # tuple - (45,56,'slovo', [3,4,56], True)


slep = [45,56,'slovo', [3,4,56], True]
# print(slep[2],slep[4]) # индексов вытащили
# print(slep[2:5:2])
# slep[2], slep[3] = slep[3], slep[1]
# print(slep)

name = 'edzen'
bh = '2000.09.18'
gender = 'male'
dar = []
dar.append(name)
dar.append(bh)
dar.append(gender)
print(dar)
dar.insert(1,'oichiev')
print(dar)
dar.extend(slep)
