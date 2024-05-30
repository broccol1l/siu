# с БОТОМ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import random

choices = ['камень', 'ножницы', 'бумага']
bot = random.choice(choices)
user_choice = input("Введите камень, ножницы или бумагу: ")

if user_choice == 'камень' and bot == 'ножницы' or user_choice == 'ножницы' and bot == 'бумага':
    print(f'Вы ПОБЕДИЛИ! Бот выбрал {bot}')
elif user_choice == 'бумага' and bot == 'камень':
    print(f'Вы ПОБЕДИЛИ! Бот выбрал {bot}')
elif user_choice == bot:
    print(f'Ничья. Бот выбрал {bot}')
else:
    print(f'Вы проиграли( Бот выбрал {bot}')

# С ПОЛЬЗОВАТЕЛЕМ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# choices = ['камень', 'ножницы', 'бумага']
# user_choice = input("Введите камень, ножницы или бумагу: ")
# print("\n" * 20)
# user_choice1 = input("Введите камень, ножницы или бумагу: ")
#
# if user_choice == 'камень' and user_choice1 == 'ножницы' :
#     print(f'Первый ПОБЕДИЛ! Первый выбрал {user_choice}. Второй выбрал {user_choice1}.')
# elif user_choice == 'ножницы' and user_choice1 == 'бумага':
#     print(f'Первый ПОБЕДИЛ! Первый выбрал {user_choice}. Второй выбрал {user_choice1}.')
# elif user_choice == 'бумага' and user_choice1 == 'камень':
#     print(f'Первый ПОБЕДИЛ! Первый выбрал {user_choice}. Второй выбрал {user_choice1}.')
# elif user_choice == user_choice1:
#     print(f'Ничья, вы вместе выбрали {user_choice1}')
# else:
#     print(f'Второй ПОБЕДИЛ! Первый выбрал {user_choice}. Второй выбрал {user_choice1}.')
