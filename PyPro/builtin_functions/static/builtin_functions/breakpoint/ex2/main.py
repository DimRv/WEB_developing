"""Пример игнорирования точек останова, путем присвоения переменной окружения 'PYTHONBREAKPOINT' = '0'"""
import os


os.environ['PYTHONBREAKPOINT'] = "0"
print("До")
breakpoint()  # точка останова будет проигнорирована
print("После")
