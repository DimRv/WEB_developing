"""Пример с возникновением ошибки ValueError"""

try:
    print(chr(1114111))
    print(chr(1114112))
except ValueError:
    print("Ошибка при обработке символа по его коду")