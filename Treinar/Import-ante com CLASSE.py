import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.__x(), point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
#Quando um objeto interage com o outro (dentro), é necessário
#apontar cada valor inicial (de __init__) em um outro método.
#EX: self.__x = x (de __init__) foi passado para getx(self)
#para poder ser chamado pelo outro objeto sem conflito de valores.
##point.__x() deu erro.... conflito! // certo -> point.getx()
