"""Пример использования any"""

print(any([None, "", False, {}, [], 0]))  # False
print(any([None, "0", False, {}, [], 0]))  # True
print(any([]))  # False
print(any(""))  # False
print(any(range(-3, 3)))  # True
