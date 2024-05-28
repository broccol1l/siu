# names = [1, 2, 3, 4, ['Hello', 3, 7]]
# print(type(names)) # Тип данных = list
# print(len(names))
# print(names[2])

# Отрицательный индекс
# names = ['Ivan', 'Pavel', 'Jordan']
# print(names[-2])
# print(names[1][2])

# SOLO
# a = ["Apple", 'Orange', 'Watermelon', 'Strawberry', 1, 2 ,3 ,4 ,5 ,6]
# print(a[1])
# print(a[3])

# print(a[0: -1 : 2])

# spisok = ['ball', 'basketball', 'football', 'volleyball', 'gandball']
# print(spisok[0:3])

# toys = ['мишка', []]

# a = '123.'
# print(len(a))

# Методы добавления
# spisok = ["privet", "poka", 1, 2, "123"]
# # spisok.extend([1, 2, 3, 4])
# spisok.insert(__index=2, __object='как дела')
# print(spisok)

# Методы для удаления

# .clear()
# .pop()
# .remove(элемент)
# spisok = ['privet', 'poka', 1, "1", 2, '123', [1,4,5]]
# # spisok.remove(1)
# # spisok.pop(-1)
# spisok[-1].pop(0) # Обращаемся к внутреннему списку
# # spisok.clear()
# print(spisok)

# Методы для изменения
# name = ['Pavel', 'Python', 'TgBot', 'Django']
# name[-1]= 1 # Заменяет
# print(name)

# .sort # Алфафитно
# .reverse() # Наоборот переворачивает

# spisok = [True, False, 'a', 'c']
# # spisok.reverse()
# print(spisok[::-1])

# Найти индекс по значению
# name = ['Pavel', 'Python', 'TgBot', 'Django']
# name_index = name.index('Pavel')
# print(name_index)
#
# name.pop(name_index)
# print(name)

# КОРТЕЖИ
# spisok = (True, False, 'a', 'c')
# spisok2 = 1, 3, 5, 'a', [1,2,3]
# spisok3 = ()
# spisok4 = ("privet", )
# spisok5 = list(spisok)
# print(spisok5, spisok)

# in
# spisok = (True, False, 'a', 'c')
# if 'a' in spisok:
#     print('есть')
# else:
#     print('нет')
#
# spisok = "привет"
# print(spisok[::-1])

# primer = [1,3,4,5,6,7, 'a', 'b']
# if 1 and 'a' in primer:
#     print("есть")

# primer = "123"
# if primer != "123" or type(primer) == str:
#     print("есть")

# a = ["oleg", 'aleksey']
# newname = input("Введите имя: ")
# a.append(newname)
# print(a)

# a = ["oleg", 'aleksey']
# newname = input("Введите имя: ")
# if newname.lower in a:
#     print('есть в списке')
# else:
#     a.append(newname.lower())
#     print(a)







