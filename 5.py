class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
