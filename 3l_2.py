def input_data(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


def main():
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_year = input('Введите год рождения: ')
    user_city = input('Введите город проживаня: ')
    user_email = input('Введите email: ')
    user_phone = input('Введите телефон: ')
    result = input_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email,
                        telephone=user_phone)
    print(f'{result}')


main()