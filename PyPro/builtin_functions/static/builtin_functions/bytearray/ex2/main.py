"""Примеры с обработкой ошибок"""

try:
    b1 = bytearray("Привет!", 'ascii', 'strict')
except UnicodeEncodeError:
    b1 = 'Ошибка при создании байтовой строки'
print(b1)  # Ошибка при создании байтовой строки

b2 = bytearray("Привет!", 'ascii', 'ignore')
print(b2)  # b'!'
b3 = bytearray("Привет!", 'ascii', 'replace')
print(b3)  # b'??????!'
b4 = bytearray("Привет!", 'ascii', 'xmlcharrefreplace')
print(b4)  # b'&#1055;&#1088;&#1080;&#1074;&#1077;&#1090;!'
b3 = bytearray("Привет!", 'ascii', 'backslashreplace')
print(b3)  # b'\\u041f\\u0440\\u0438\\u0432\\u0435\\u0442!'
b3 = bytearray("Привет!", 'ascii', 'namereplace')
print(b3)  # b'\\N{CYRILLIC CAPITAL LETTER PE}\\N{CYRILLIC SMALL LETTER ER}\\N{CYRILLIC SMALL LETTER I}\\N{CYRILLIC SMALL LETTER VE}\\N{CYRILLIC SMALL LETTER IE}\\N{CYRILLIC SMALL LETTER TE}!'

