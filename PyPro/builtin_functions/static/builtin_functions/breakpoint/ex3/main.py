"""Пример использования собственной функции обработки точек останова"""
import os


os.environ['PYTHONBREAKPOINT'] = "print"

print("До")
breakpoint("Останов")  # print будет обработчиком точки останова
print("После")
