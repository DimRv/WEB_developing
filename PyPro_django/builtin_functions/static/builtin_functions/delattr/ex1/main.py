"""Пример использования встроенной функции delattr"""


class C:
    attrib = "attr"
    attrib2 = 'attr2'


print([i for i in C.__dict__ if not i.startswith('__')])  # ['attrib', 'attrib2']
delattr(C, 'attrib')
del C.attrib2
print([i for i in C.__dict__ if not i.startswith('__')])  # []
