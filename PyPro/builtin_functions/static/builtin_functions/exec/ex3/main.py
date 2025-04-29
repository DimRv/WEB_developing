"""Пример работы exec с замыканием closure"""

from types import CellType


def a():
    inner = 1

    def b():
        nonlocal inner
        print(inner)
    return b


code = a().__code__  # создаем объект code
exec(code, closure=(CellType(7),))  # 7
