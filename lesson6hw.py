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