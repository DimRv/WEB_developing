"""Пример использования встроенной функции filter()"""

arr = list(range(8))
new_arr = list(filter(lambda x: x % 2 == 0, arr))  # отсеиваем нечетные числа
new_arr2 = list(filter(None, new_arr))  # отсеиваем False элементы
print(arr)  # [0, 1, 2, 3, 4, 5, 6, 7]
print(new_arr)  # [0, 2, 4, 6]
print(new_arr2)  # [2, 4, 6]

