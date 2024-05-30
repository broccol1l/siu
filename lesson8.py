# lambda - анонимные функции, без названия
# a = lambda x: x**2
# print(a(10))
#
# def stepen(x):
#     return int(x)**2
# a = stepen(input('Число: '))
# print(a)

# s = lambda a,b: a*b
# print(s(3, 4))

#map()
# x = [1, 2, 3, '4']
# a = map(lambda d: d*2, x)
# print(list(a))

#filter()
# x = [1, 2, 3, '4']
# a = filter(lambda d: d*2 == 4, x)
# print(list(a))
#
# x = ['Jordan', 'Pavel', 'Pasha', 'Jacky']
# a = list(filter(lambda l: 'J' in l, x))
# print(a)

# SOLO
# x = [1, 2, 4, 8, 123123, -3, -2, 1, -1221, -235]
# y = filter(lambda d: d >= 0, x)
# print(list(y))
# requests
# get - получение данных, post - отправка данных
import requests

response = requests.get('ссылка')
print(response.text)
