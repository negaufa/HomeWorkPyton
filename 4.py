from random import randint

my_list = [randint(-10, 10) for _ in range(10)]

my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список {my_list}')
print(f'Новый список, не имеющий повторений {my_new_list}')
