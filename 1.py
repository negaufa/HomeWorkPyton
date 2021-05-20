from sys import argv


def get_salary(pay_for_hour, bonus, work_time):
    try:
        salary = int(pay_for_hour) * int(work_time) + int(bonus)
    except ValueError:
        print('Not a number')
    return salary


def main():
    script_name, pay_for_hour, bonus, work_time = argv
    salary = get_salary(pay_for_hour, bonus, work_time)
    print(f'Зарплата отрудника составляет {salary}')


main()
