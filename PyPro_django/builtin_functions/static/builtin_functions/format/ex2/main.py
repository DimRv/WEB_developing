"""Пример создания класса с __format__ - форматирует вывод по шкале Цельсия, Фаренгейта и Кельвина"""


class Temperature:
    def __init__(self, val):
        self.val = float(val)

    def __format__(self, format_spec):
        match format_spec:
            case 'c':
                return f"{self.val: .2f} {chr(176)}C"
            case "f":
                return f"{(self.val * 9 / 5) + 32: .2f} {chr(176)}F"
            case 'k':
                return f"{self.val + 273.15: .2f} K"


t = Temperature(36.6)
print(format(t, "c"))  # 36.60 °C
print(format(t, "f"))  # 97.88 °F
print(format(t, "k"))  # 309.75 K
