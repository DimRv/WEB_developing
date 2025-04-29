"""Пример использования встроенной функции exec с глобальными и локальными переменными"""


def f():
    expression = """
print(a+b)
print(a-b)
"""
    exec(expression, {"a": 4}, {"b": 3})


f()  # 7 1
