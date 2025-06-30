"""Пример применения встроенной функции abs с объектами"""


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


coord = Coord(-6, -8)
print(abs(coord))  # 10.0
