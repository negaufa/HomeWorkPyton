users_lst = list(input('Введите значения списка, используйте пробел в качестве разделителя: ').split())
end = len(users_lst) - len(users_lst) % 2
users_lst[:end:2], users_lst[1:end:2] = users_lst[1:end:2], users_lst[:end:2]
print(users_lst)

