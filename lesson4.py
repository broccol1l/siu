# ЦИКЛЫ
# for - оператор

# nabor = ('1', 2, 'a')
# for b in nabor:
#     print(b)

# Табуляция важна!!!!!!!!!!!!!!!

# my_list = (6, 'a', '2')
# for item in my_list:
#     print(item)
#     print(f'Всего {len(my_list)} элементов')

# my_list = (6, 'a', '2')
# for item in my_list:
#     print(item)
# print(f'Всего {len(my_list)} элементов')

# my_list = (6, 4, '2')
# for t in my_list:
#     print(t+2)

# range() - количество итераций(повторений)

# my_tuple = (6, 4, "2")
# count = 0
# for i in range(1, 100, 2):
#     count = count + 1
#     print(count)
#     print(f'{my_tuple}')

# names = ["pavel", 'ivan', 'jordan', 5]
# for i in range(1, 20):
#     if 'ivan' in names:
#         print('ivan есть в списке')
#     else:
#         print('о ком вы')

# WHILE - работает сколько раз угодно если передать условие.

# p = ['m', 'my', 23]
# i = 0
# while i < len(p):
#     print(p[i])
#     i = i + 1

# names = ['Ivan', 'Pavel', 'Jordan']
# while True:
#     print('{}'.format(names[0::2]))


# names = ['oleg', 'masha']
# # while True:
# #     new = input('Кого добавим?: ')
# #     if new == 'выход':
# #         exit(0)
# #         # break
# #     else:
# #         names.append(new)
# #         print(names)

# names = []
# contacts = []
# services = []
#
# menu = input('Введите номер действия:\n'
#              '1 - Добавить имя\n'
#              '2 - Добавить номер\n'
#              '3 - Добавить услугу\n')
# if menu == '1':
#     new_name = input('Введите имя: ')
#     names.append(new_name)
#     print(f'Новое имя {new_name} добавлен в список')
#     print(names)


# names = []
# contacts = []
# service = []
# while True:
#     new_name = input('Введите имя: ')
#     if new_name in names:
#         print("Имя успешно введено")
#     else:
#         names.append(new_name)
#
#     new_contact = input('Введите номер: ')
#     if new_contact in contacts:
#         print('Номер успешно введен')
#     else:
#         contacts.append(new_contact)
#     new_service = input('Введите сервис: ')
#
#     if new_service in service:
#         print('Сервис был введен')
#     else:
#         contacts.append(new_service)
#         print(names, contacts, service)

# count = 0
# while count < 5:
#     print(count)
#     count += 1
#
# for i in range(5):
#     print(i)

# a = 0
# while a < 15:
#     print(a)
#     a = a + 2

from time import sleep

countdown = [4, 3, 2, 1, 0]


for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")