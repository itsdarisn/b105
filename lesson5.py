# Изменяемые и неизменяемые
# integer = 123, 34 - Ne
# float = 1.5, 4545.432 Ne 
# boolean - True, False ,Ne 
# string - "asfe" Ne 
# tuple - () - Ne - кортеж 
# frozenset() - {} - Ne 
# set - {} - Iz 
# list -[] - Iz - список 
# dictionary - {} - Iz - словарь 

# tuple - ()
# names1 = ('Baha','Jeka','Madi')
# names2 = ['Baha','Jeka','Madi']
# names2[0] = 'Gennadii'
# print(names1.__sizeof__())
# print(names2.__sizeof__())

# dict = {}
# names = {
#     'Alina': ["алина родной","где зп",23, 45],
#     'alina': (45, 54, "aitishka", "shkola"),
#     2000: 'двухтысячные',
#     2.3455:{"пн":1, "вт":2}
# }
# print(names)
# for i in names.items():
#     print(i)

# перебираемые и неперебираемые - проводить цикл или нельзя
# индексирумые и неиндексируемые
# dict, tuple, list, str, set - можно 
# int, float, bool, - нельзя
# numbers = [3,34,56,67]
# for i in numbers:
#     print(i)

# print(type(True))
# print(type(345))
# print(type([{(45,546,67,78)}]))

# name = tuple('45')
# print(name)
# print(type(name))

# set() - frozenset() - множества - уникальные значения
# неупорядоченный тип данных 
# names = {'Baha','Jeka','Madi'}
# print(names)

# name = set('hello')
# print(name)

# Массив - java, kotlin, php, c 

# while - пока
# for - для 
# n = [34,45,67,99]
# for i in n:
#     # i = временная переменная 
#     i += 1
#     print(i)

# # range() - функция генерации чисел
# for i in range(1,6):
#     print(f'{i},i love python')

# a = 0
# while a <= 10:
#     a += 1
#     print(f"{a}.love")

# a = 1
# while a < 5:
#     print('uslovie verno')
#     a = a + 1
# else:
#     print('uslovie neverno')