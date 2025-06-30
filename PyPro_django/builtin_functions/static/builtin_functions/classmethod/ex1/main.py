"""Пример использования встроенной функции classmethod"""


class MyClass:
    value = 0


def method(cls):
    cls.value += 1


MyClass.method = classmethod(method)
print(type(method), type(MyClass.method))  # &lt;class 'function'> &lt;class 'method'>
print(MyClass.value)  # 0
MyClass.method()
MyClass.method()
print(MyClass.value)  # 2
