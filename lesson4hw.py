# Упр 5. Сдаем бутылки

# small_bottles = 0.10
# big_bottles = 0.25
#
# amount_smallbottles = int(input('Введите количество бутылок объемом 1 литр или меньше: '))
# amount_bigbottles = int(input('Введите количество бутылок объемом больше 1 литра: '))
#
# total_amount = (small_bottles * amount_smallbottles) + (big_bottles * amount_bigbottles)
# print("Сумма, которую можно выручить: ${:.2f}".format(total_amount))

# Упр 6. Налоги и чаевые

# total_amount = float(input("Введите сумму заказа:$"))
# tax = 10
# tips = int(input("Сколько процентов от стоимости хотите добавить для обслуживания: "))
#
# percentage1 = tax / 100
# result_tax = percentage1 * total_amount
# percentage2 = tips / 100
# result_tips = percentage2 * total_amount
#
# summary = (percentage1 * total_amount) + (percentage2 * total_amount) + total_amount
# print(f"\nНалог = {tax}%, Общая сумма Налога = ${result_tax:.2f}",
#       f"\nЧаевые = {tips}%, Общая сумма Чаевых = ${result_tips:.2f}",
#       f"\nИтог = ${summary:.2f}")

# Упр 7. Сумма первых n положительных чисел

# num = int(input('Введите натуральное положительное число: '))
# if num <= 0:
#       print('Повторите снова')
# else:
#       total_sum = (num) * (num + 1) // 2
#       print(f'Сумма натуральных чисел от 1 до {num} = {total_sum} ')

# Упр 8. Сувениры и безделушки

# item1 = int(input("Введите количество сувениров: "))
# item2 = int(input("Введите количество безделушек: "))
#
# souvenir = 75
# bezdelushka = 112
#
# total_sum = (item1 * souvenir) + (item2 * bezdelushka)
#
# print(f'\nОбщий вес посылки равен {total_sum}')

# Палиндром

# while True:
#     word = str(input("Введите палиндром или выход: "))
#     a = word[::-1]
#     if word == a:
#         print('Палиндром')
#     elif word.lower() == "выход":
#         print('Вы вышли')
#         break
#     else:
#         print('Не палиндром')

# Таблица умножения

# num = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
