"""Пример работы функции ascii"""

print(ascii("Hello, World!"))  # 'Hello, World!'
print(ascii("Привет, Мир!"))  # '\u041f\u0440\u0438\u0432\u0435\u0442, \u041c\u0438\u0440!'
print(ascii(["Hello", "Привет"]))  # ['Hello', '\u041f\u0440\u0438\u0432\u0435\u0442']
print(ascii(__doc__))  # '\u041f\u0440\u0438\u043c\u0435\u0440 \u0440\u0430\u0431\u043e\u0442\u044b \u0444\u0443\u043d\u043a\u0446\u0438\u0438 ascii'
