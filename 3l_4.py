def my_func_1(x, y):
    result = 1 / x ** abs(y)
    return result


def my_func_2(x, y):
    if y == 0:
        return 1
    else:
        if y < 0:
            return 1 / my_func_2(x, -y)
        else:
            return x * my_func_2(x, y - 1)


def main():
    x = 5
    y = -2
    result_1 = my_func_1(x, y)
    result_2 = my_func_2(x, y)
    print(result_1, result_2)


main()