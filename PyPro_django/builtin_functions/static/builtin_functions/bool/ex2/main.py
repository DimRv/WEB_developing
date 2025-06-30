"""Пример преобразования __bool__ объекта,
Для отрицательных значений MyInt возвращает False
"""


class MyInt(int):
    def __init__(self, val):
        self.val = val

    def __bool__(self):
        return self.val > 0


int1 = -5
print(bool(int1))  # по умолчанию True
my_int = MyInt(-5)
print(bool(my_int))  # теперь False
