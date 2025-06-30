"""Пример использования встроенной функции enumerate"""

months = ['январь', 'февраль', "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

for num, month in enumerate(months, 1):
    info = f"{num} месяц - {month}" if num > 9 else f"0{num} месяц - {month}"
    print(info)
