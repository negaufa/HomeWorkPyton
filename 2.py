class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.area = self.__length * self.__width

    def weight(self, weight, thickness):
        return (self.area * weight * thickness)


road = Road(3, 5)
result = road.weight(25, 3)
print(result)
