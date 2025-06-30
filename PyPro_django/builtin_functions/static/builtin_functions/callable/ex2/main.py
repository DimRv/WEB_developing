"""Пример создания вызываемого объекта"""


class MyInt(int):
    def __init__(self, val):
        self.val = val

    def __call__(self, val):
        return MyInt(self.val ** val)


my_int = MyInt(5)
print(callable(my_int))
my_int = my_int(3)
