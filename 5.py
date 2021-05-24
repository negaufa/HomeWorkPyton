user_string = input('Введите строку чисел, разделённых пробелом. ')
result = 0
with open('task_5.txt', 'r+') as f:
    f.writelines(user_string)
    numbers = f.readline()

for i in numbers:
    try:
        result += int(i)
    except ValueError:
        "Неверный формат данных"
print(result)
