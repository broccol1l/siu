# Сделать Hotel management system

# 1- У меня должно быть 3 функции
# (Добавить клиента, Удалить клиента, Увидеть занятые номера)
# 2- Для добавления клиента вывести занятые номера и
# добавить в словарь:
# ключ(имя клиента: значение(номер комнаты)
# 3- При удалении клиента удалить введенное имя из базы
# 4- При выводе занятых номеров должен выводиться список
# 5- Цикл

clients = {}

def add_client():
    # print('Занятые номера: ', clients)
    name = input('Введите имя, которое хотите добавить: ')
    number = int(input('Введите номер комнаты, которое хотите добавить: '))
    if name.lower() in {i.lower() for i in clients}:
        print('Это имя уже занято')
    elif number in clients.values():
        print('Этот номер уже занят', clients.values())
    else:
        clients[name.lower()] = number
        print(f'Имя {name} и номер комнаты {number} успешно введены')


def remove_client():
    print(clients)
    remove_name = input('Введите имя, которое хотите удалить: ')
    if remove_name.lower() not in {i.lower() for i in clients}:
        print('Такое имя не существует')
    else:
        clients.pop(remove_name.lower())
        print(f"{remove_name} успешно удален/a")


def existing_client():
    print('Занятые номера:', clients.values())


while True:
    menu = int(input('\nВведите номер действия'
                     '\n1-Добавить клиента'
                     '\n2-Удалить клиента'
                     '\n3-Увидеть занятые номера'
                     '\n4-Выйти: '))
    if menu == 1:
        add_client()
    elif menu == 2:
        remove_client()
    elif menu == 3:
        existing_client()
    elif menu == 4:
        print('Вы успешно вышли')
        break
    else:
        print('Вы ввели не тот номер')




