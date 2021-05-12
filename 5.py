rait_lst = [17, 15, 13, 13, 22]
users_rait = int(input('Введите рейтинг: '))
rait_lst.append(users_rait)
rait_lst.sort(reverse=True)
print(f'Итоговый рейтинг: {rait_lst}')

