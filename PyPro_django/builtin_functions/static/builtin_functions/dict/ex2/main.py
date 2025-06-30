"""Создание объекта, способного к преобразованию к словарю"""


class DictCreator:
    def __init__(self, x):
        self.x = x

    def keys(self):
        return list(range(self.x))

    def __getitem__(self, item):
        return item * 2


c = DictCreator(5)
print(dict(c))  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}