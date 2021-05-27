from time import sleep


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in range(len(self.__color)):
            print(f'Светофор переключается \n '
                  f'{self.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(10)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
