my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_new_list = [el for num, el in enumerate(my_list) if num != 0 and my_list[num] > my_list[num - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
