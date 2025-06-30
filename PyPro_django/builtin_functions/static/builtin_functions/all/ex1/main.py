"""Пример использования встроенной функции all"""


print(all([True, ' ', 5]))  # True
print(all({True, '', 5}))  # False
print(all((True, ' ', 0)))  # False
print(all([]))  # True
print(all(range(-3, 3)))  # False
print(all("Hello, World!"))  # True
print(all(""))  # True
