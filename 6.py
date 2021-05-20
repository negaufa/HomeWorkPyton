from itertools import count, cycle


def count_func(start, stop):
    for el in count(int(start)):
        if el > int(stop):
            break
        else:
            print(el)


def cycle_func(stop, my_list):
    iterable = cycle(my_list)
    count = 0
    while count < stop:
        print(next(iterable))
        count += 1


def main():
    start = int(input("Введите стартовое значение: "))
    stop_count = int(input("Введите конечное значение: "))
    count_func(start, stop_count)
    print('Генерация чисел завершена')
    my_list = [15, 2, 1]
    stop_cycle = int((input("Введите количетсво итераций: ")))
    cycle_func(stop_cycle, my_list)
    print('Итерация списка завершена')


main()
