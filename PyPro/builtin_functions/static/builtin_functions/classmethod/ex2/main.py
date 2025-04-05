"""Пример использования функции classmethod через декораторы"""


class MyClass:
    value = 0

    @classmethod
    def increase(cls):
        cls.value += 1


print(MyClass.value)  #0
MyClass.increase()
MyClass.increase()
print(MyClass.value)  #2
