"""Пример использования функции classmethod"""


class MyClass:
    value = 0

    @classmethod
    def increase(cls):
        cls.value += 1


print(MyClass.value)
MyClass.increase()
MyClass.increase()
print(MyClass.value)
