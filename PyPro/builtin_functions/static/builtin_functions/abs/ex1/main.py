"""Пример работы abs с числами"""

abs1 = abs(4)
abs2 = abs(-4)
abs3 = abs(-3.5)
abs4 = abs(-4 + 3j)

print(type(abs1), abs1)  # <class 'int'> 4
print(type(abs2), abs2)  # <class 'int'> 4
print(type(abs3), abs3)  # <class 'float'> 3.5
print(type(abs4), abs4)  # <class 'float'> 5.0
