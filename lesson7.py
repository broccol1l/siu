# Функции - шаблон действия, который закрепляем в блоке
# def say_hello():
#     print('Hello World')
#
# say_hello()

# return - результат
# def calc():
#     a = 1 + 20
#     return a
#
# test = calc()
# print(test)

#Параметры функций
# a и b - обязательно, c - необязательно
# def spam2(a, b, c =7):
#     print(a+b+c)
# spam2(3, 2,)

# TZ
# def i(a, b):
#     print(a+b)
# i(3, 5)


# args - задать любое количество аргументов
# def spam1(*args):
#     summa = args[0] + args[1] + args[2]
#     return summa
# print(spam1(1,2,3,'Hello'))

#**kwargs - so slovaryom
# def spam1(**kwargs):
#     return kwargs
# print(spam1(name= "my1", age = 23))

#TZ
while True:
    def calc():
        num = int(input('Введите число: '))
        # return num
        if num % 2 == 0:
            print('Четный')
        elif num % 2 != 0:
            print('Нечетный')
        else:
            print('Повтори снова')

    calc()