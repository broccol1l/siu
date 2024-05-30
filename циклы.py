names = []
numbers = []
services = []

while True:
    # Меню пользователя
    menu = input("Выберите действие:\n"
                 "1- Добавить имя\n"
                 "2- Добавить номер\n"
                 "3- Добавить услугу\n"
                 "4- Показать все списки\n"
                 "5- Выход")
    # Добавление имени
    if menu.lower() == "имя":
        new_name = input("Введите имя: ")
        # проверка на наличие имени в списке
        if new_name in names:
            print("Данное имя уже занято")
        elif new_name.isdigit():
            print("Вы ввели числа. Введите имя")
        else:
            names.append(new_name)
            print(f"Имя {new_name} добавлено")
            print(names)
    # Добавление номера
    elif menu.lower() == "номер":
        new_number = input("Введите номер: ")
        if new_number in names:
            print("Данный номер уже имеется в списке")
        elif new_number.isalpha():
            print("Введи номер используя только цифры")
        else:
            numbers.append(new_number)
            print(f"Номер {new_number} добавлен")
            print(numbers)
    # Добавление услуги
    elif menu.lower() == "услуги":
        new_service = input("Введите услугу: ")
        if new_service in services:
            print("Данный сервис уже имеется в списке")
        else:
            services.append(new_service)
            print(f"Номер {new_service} добавлен")
            print(services)
    elif menu.lower() == "списки":
        print(f"Имена: {names}\n"
              f"Номера: {numbers}\n"
              f"Услуги: {services}")
    elif menu.lower() == "выход":
        print("Приложение закрыто")
        break
    else:
        print("Такой функции нет")