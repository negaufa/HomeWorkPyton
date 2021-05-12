users_str = list(input('Введите значения списка, используйте пробел в качестве разделителя: ').split())
count_str = 1
count_lst = 0
while count_str < len(users_str) + 1:
    print(f'{count_str} {users_str[count_lst][:10]}')
    count_str += 1
    count_lst += 1
