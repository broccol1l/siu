contacts = ["Ramazan", "909379035", "Messi", "909999999", "Ronaldo", "778889900"]

menu = input("Ваши действия: 1-Добавить, 2-Удалить, 3-Изменить: ")

if menu == "1":
    new_name = input('Введите имя нового контакта: ')
    new_phone = input('Введите номер нового контакта: +998')

    if new_name in contacts and new_phone in contacts:
        print("Это имя или номер уже существует в списке контактов.")
    else:
        contacts.append(new_name)
        contacts.append(new_phone)
        print(f"Успешно добавлено имя {new_name} и номер {new_phone}")
        print(contacts)

elif menu == "2":
    delete_name = input("Введите имя контакта, которое хотите удалить: ")
    delete_phone = input("Введите номер контакта, которое хотите удалить: ")

    if delete_name in contacts and delete_phone in contacts:
        contacts.remove(delete_name)
        contacts.remove(delete_phone)
        print(f"Успешно удалено имя {delete_name} и номер {delete_phone}")
        print(contacts)
    else:
        print("Имя или номер контакта не найдены.")

elif menu == "3":
    change_name = input("Какое имя хотите изменить?: ")
    if change_name in contacts:
        new_name = input('На какое имя?: ')
        contacts[contacts.index(change_name)] = new_name
    else:
        print("Такое имя не найдено.")

    change_phone = input("Какой номер хотите изменить?: ")
    if change_phone in contacts:
        new_phone = input('На какой номер?: ')
        contacts[contacts.index(change_phone)] = new_phone
    else:
        print("Такой номер не найден.")
    print(contacts)
else:
    print('Повторите снова')
