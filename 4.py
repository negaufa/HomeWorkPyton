class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула  {self.direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'превышении скорости!'
        else:
            return f'Скорость автомобиля {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'превышении скорости!'
        else:
            return f'Скорость автомобиля {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(160, 'зеленый', 'Audi', False)
ford = TownCar(30, 'синий', 'ford', False)
lada = WorkCar(10, 'черный', 'Lada', True)
nissan = PoliceCar(110, 'белый', 'Nissan', True)

print(f'{ford.turn("вправо")}, и {ford.stop()}')
print(f'{audi.go()}  {audi.show_speed()}')
print(f'{ford.name}  имеет {ford.color} цвет')
print(f' {audi.name} это машина пренадлежит полиции {audi.is_police}')
print(f' {nissan.name} это машина пренадлежит полиции  {lada.is_police}')
print(audi.show_speed())
print(ford.show_speed())
print(nissan.show_speed())
