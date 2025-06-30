"""Пример использования встроенной функции dict"""


d0 = dict()  # пустой dict
d1 = dict((('one', 'один'), ('two', 'два')))  # dict из итерируемого объекта
d2 = dict(one='один', two='два')  # dict из **kwargs

print(d0)  # {}
print(d1)  # {'one': 'один', 'two': 'два'}
print(d2)  # {'one': 'один', 'two': 'два'}
