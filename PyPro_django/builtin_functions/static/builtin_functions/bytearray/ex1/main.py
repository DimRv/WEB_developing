"""Пример использования встроенной функции bytearray()"""


b0 = bytearray()  # Пустая байтовая строка
print(type(b0), b0)  # b''
b1 = bytearray(5)  # Байтовая строка, заполненная нулями длины 5
print(print(type(b1), b1))  # b'\x00\x00\x00\x00\x00'
b2 = bytearray(range(256))  # байтовые строки могут содержать целые числа в диапазоне от 0 до 255 включительно.
print(type(b2), b2)  # символы ASCII от 30 до 127 отображаются
b3 = bytearray("Hello!", 'ascii')  # создание байтовой строки из str
print(type(b3), b3)  # b'Hello!'
