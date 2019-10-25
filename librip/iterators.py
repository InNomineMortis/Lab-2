from types import GeneratorType


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        ignore_case = kwargs.get("ignore_case")
        if ignore_case is None:
            ignore_case = False
        self.ignore_case = ignore_case
        self.already = []
        if isinstance(items, GeneratorType):
            self.items = items
        else:
            self.items = iter(items)
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__
        self.current = self.items.__next__()
        current = self.current
        if self.ignore_case:
            current = current.lower()
        if current in self.already:
            self.__next__()
        else:
            self.already.append(current)
        return self.current

    def __iter__(self):
        return self
