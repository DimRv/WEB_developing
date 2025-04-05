"""Пример использования встроенной функции complex"""


a = complex(5)
b = complex('-4+3j')
c = complex(real=5, imag=2)
d = complex()

print(a)  # (5+0j)
print(b)  # (-4+3j)
print(c)  # (5+2j)
print(d)  # 0j
