result = 0


def get_sum(*args):
    result = sum(args)
    return result


while True:
    user_string = map(int, input('Введите строку чисел, разделённых пробелом. ').split())
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: ').upper() == 'Q':
        result += get_sum(*user_string)
        print(f'Сумма чисел {result}')
        break
    else:
        result += get_sum(*user_string)
        print(f'Сумма чисел {result}')