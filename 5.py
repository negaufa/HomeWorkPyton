from functools import reduce

my_list = reduce(lambda a, b: a*b, [el for el in range(100, 1001) if el % 2 == 0])
print(f'Результат перемножения всех элементов списка {my_list}')