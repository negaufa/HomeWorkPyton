users_lst = []
name_lst = []
price_lst = []
count_lst = []
unit_lst = []
while input("Если вы хотите ввести номер товара, введите + ") == '+':
    number = int(input("Введите номер товара: "))
    product_name = input("Введите название товара: ")
    name_lst.append(product_name)
    product_price = input("Введите цену товара: ")
    price_lst.append(product_price)
    product_count = input('Введите количество товара: ')
    count_lst.append(product_count)
    product_unit = input("Введите единицу измерения товара: ")
    unit_lst.append(product_unit)
    users_dict = {'Название': product_name, 'Цена': product_price, 'Количество': product_count,
                  'Единица измерения': product_unit}
    # Формируется кортеж
    users_tuple = (number, users_dict)
    # Формируется структура данных "Товары"
    users_lst.append(users_tuple)
    # Формирование аналитики о товарах
    final_dict = {'Название': name_lst, 'Цена': price_lst, 'Количество': count_lst,
                  'Единица измерения': unit_lst}
print(users_lst)
print('_______________________________________________________________________________________________________________')
print(final_dict)
