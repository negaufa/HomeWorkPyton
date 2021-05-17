def my_segmentation(num1, num2):
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Деление на 0 запрещено'
    return result


print(f'Результат выполнения функции - {my_segmentation(int(input()), int(input()))}')
