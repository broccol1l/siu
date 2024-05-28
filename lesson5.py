# List comprehension

# nums = [1,2,3,4]
# num = [ i*2 for i in nums]
# string.upper() - из 'privet' в 'PRIVET'
# Using with for
# name = 'Pasha'
# n = []
#
# for item in name:
#     n.append(item)
#
# print(n)

# Using List comprehension

# name = 'Pasha'
# n = [x for x in name]
# print(n)

# Example

# my_list = [1, 'a', 2, 4.5]
# my = [i+2 for i in my_list if type(i) == int and type(i) == float]
# print(my)

# Example

# nums = [i for i in range(1, 11)]
# chothnie = [num for num in nums if num % 2 == 0]
# nechotnie = [num for num in nums if num % 2 != 0]
# print(chothnie, nechotnie)

# Practise

# names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
# answer = [i[0] for i in names]
# print(answer)

# nums = [1, 2, 3]
# my_list = [i for i in range(1, 11) if i in nums]
# print(my_list)

# TZ
# nums1 = [i for i in range(1, 21)]
# nums2 = [i for i in nums1 # range(1, 21) if i % 2 == 0]
# print(nums2)

# TZ
# my tz
# names = []
# while True:
#     name = input("Введите имя: ")
#     print("Имя успешно введено")
#     if name.lower() in names:
#         print('Такой user уже есть')
#     else:
#         names.append(name)
#         print(names)

# teacher's tz

# username = ["Oleg"]
# while True:
#
#     name = input("Введите имя: ")
#     if name.lower() in [i.lower() for i in username]:
#         print('Данное имя уже введено')
#     elif name.lower() == "выход":
#         print('вы вышли')
#         break
#     elif name.lower() not in [i.lower() for i in username]:
#         username.append(name)
#         print("Имя успешно добавлено")
#         print(username)
#     else:
#         print("Ошибка")
#
#


my_list = [1,'a', 2, 4.5]
for spam in my_list:
    print(spam)





