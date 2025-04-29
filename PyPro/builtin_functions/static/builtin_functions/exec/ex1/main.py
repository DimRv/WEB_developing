"""Пример использования встроенной функции exec"""

expression = """
import random
a = random.randint(2, 9)
print(a)
"""

exec(expression)  # число от 2 до 9
