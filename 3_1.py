month_number = int(input('Введите календарный номер месяца от 1 до 12: '))
season = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
index = 0
index2 = 0
for i in season:
    try:
        index2 = i.index(month_number)
    except ValueError:
        index2 = -1
    if index2 != -1:
        break
    index += 1
print(f'Ваше время года - {season[index][0]}')
