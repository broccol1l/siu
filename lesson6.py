# Словари
# x = {'name': 'Pasha', 'job': 'TGbot creator'}
# print(x['name'])

# Example
# data = {'name': ['Jordan', 'Pavel'],
#         'age': (12, 21),
#         'job': 'programmers'}
# print(data['name'][0], data['job'][-1])

# x = input('Введите имя')
# a = {'name':x}
# print(x)

# Методы словарей
# .values - значения ключей
# .keys() - выдаст ключи словаря
# .items() - выдаст ключи, значения

#Example
# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
#
# if 21 in instructor.values():
#     print('Да есть')
# else:
#     print('Не понимаю о чем вы')

# instructor = {'name': 'Jordan', 'age': 21, 'job': 'programmer'}
#
# if 'name' in instructor:
#     print('Да есть')
# else:
#     print('Не понимаю о чем вы')

# Добавление новых ключ-значений
# users = {}
# users['name'] = 'Jordan'
# print(users)
# print(users['name'])

# users = {}
# users['name'], users['age'] = 'Jordan', 21
# print(users)

# users = {}
# users['name'], users['age'] = 'Jordan', 21
# users.update(age=22, job='Junior', email = 'Jordan@gmail.com')
# print(users)

# Замена
# users = {'name': 'Jordan'}
# print(users)
# users['name'] = 'Pavel'
# print(users)

#Example

# cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Mnogo', 'Otkritie': '2007'}}
# cafees['Evos']['Кухня'] = 'Fast Food'
# print(cafees)

# cafees = {'Evos': {'Gorod': 'Tashkent', 'Filialov': 'Mnogo', 'Otkritie': '2007'}}
# cafees['Кухня'] = 'Fast Food'
# print(cafees)

# Методы для удаления
# .clear()
# .pop('name')
# .popitem()
# .get()

# my_dict = {'name': 'Jordan'}
# my_dict.clear()
# print(my_dict)

#Sets
# nums2 = set({'Hello', 'Hello', 'myname', 2, 2, 0})
# print(nums2)

# list1 = ['Jordan', 'Pavel', 'Jordan', 'Jordan', 'Sasha']
# counter = 0
# for i in list1:
#     if i == 'Jordan':
#         counter += 1
#     else:
#         print('')
#
# print(counter)

# my = ['2', '33', '33', 2, 'TgBot']
# my2 = set(my)
# print(my2)

# Цикл for со словарем - обязательно указать что вывести
# instructor = dict(name='Jordan', age=32, job='Python developer') # ???????????????????????
#
# for v in instructor.keys():
#     print(v)

# instructor = dict(name='Jordan', age=32, job='Python developer') # ???????????????????????
#
# for v in instructor.values():
#     print(v)

# instructor = dict(name='Jordan', age=32, job='Python developer') # ???????????????????????
#
# for k,v in instructor.items():
#     print(k, ":", v)

#TZ


all_sklad = {'Весь склад': {'apple': 3}}
all_products = {'Корзина': {}}

while True:
    admin = int(input('Что хотите сделать? 1-Добавить, 2-Заменить, 3-Удалить, 4-Корзина или 5-Выйти: '))
    if admin == 1:
        product_name = input('Название продукта: ')
        if product_name in all_sklad['Весь склад']:
            product_count = int(input('Количеств продукта: '))
            if product_count <= all_sklad['Весь склад'][product_name]:
                all_sklad['Весь склад'][product_name] -= product_count
                all_products['Корзина'][product_name] = product_count
                print(f'Товар {product_name} добавлен в корзину !')
            else:
                print(f'У нас нету такого кол-ва. Есть {all_sklad["Весь склад"][product_name]}.')
        else:
            print(f'У нас нету - {product_name}')
    elif admin == 2:
        print(all_products)
        old_product = input('Название продукта для замены?: ')
        if old_product in all_products['Корзина']:
            # del all_products['Корзина'][old_product]
            product_change = input('Новое название продукта?')
            product_count = int(input('Новое кол-во: '))
            all_products['Корзина'][product_change] = product_count
            print('Товар заменен !')
        else:
            print('Продукт не найден')
    elif admin == 3:
        print(all_products)
        delete_product = input('Какой продукт хотите удалить?: ')
        if delete_product in all_products['Корзина']:
            all_products['Корзина'].pop(delete_product)
            print(all_products)
        else:
            print('Продукт не найден')
    elif admin == 4:
        print('Текущая корзина: ', all_products['Корзина'])
    elif admin == 5:
        print('Вы успешно вышли!')
        break
    else:
        print('Введите снова')


