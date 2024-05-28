# List comprehension HW

# 1 - Список всех чисел от 1 до 100, которые делятся на 3.

# nums = [i for i in range(1, 101)]
# divide = [i for i in nums if i % 3 == 0]
# print(nums)
# print(divide)

# 2 - Получение списка всех палиндромов из списка words

# words = ["radar", "car", "aboba", "ded", 'дядя Альберт']
# palindrome = [word for word in words if word == word[::-1]]
# print("Слова со списка: ", words)
# print("Палиндромы: ", palindrome)

# 3 - Список всех кубов чисел от 1 до 10

# nums = [i for i in range(1, 11)]
# cube = [i ** 3 for i in nums]
# print(nums)
# print(cube)

# 4 - список всех возможных комбинаций двух списков

# alphabet = ['a', 'b', 'c']
# integer = [1, 2, 3]
# comb = [(a,b) for a in alphabet for b in integer]
# print(comb)

# 5 - Вывести список где будет буква а в именах

# names = ["artur", "ramazan", "sergey", "john", "muslim", "albert",]
# alpha = [i for i in names if "a" in i]
# print(names)
# print(alpha)

# 6 - выводит положительные и отрицательные числа как отдельные списки

# numbers = [-1, 2, 7, 9, 4, 345, -3, 4, -18, -700, -19, 10, -9]
# positive = [i for i in numbers if i > 0]
# negative = [i for i in numbers if i < 0]
# print(numbers)
# print(positive)
# print(negative)

# 7 - Делает большие слова маленькими

# slova = ["ARTUR", "ALBERT", "RAMAZAN", "SILA"]
# loweralpha = [word.lower() for word in slova]
# print(loweralpha)


