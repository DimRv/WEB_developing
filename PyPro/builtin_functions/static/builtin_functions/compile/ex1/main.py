"""Пример использования вcтроенной функции compile"""


x = compile('x = 1\nz = x + 3\nprint(z)', '&lt;string&gt;', 'exec')
print(x, type(x))
exec(x)  # 4
