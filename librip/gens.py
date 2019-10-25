import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def field(items, *args):
    if len(args) == 0:
        for item in items:
            yield item
    for item in items:
        if len(args) == 1:
            f = item.get(args[0])
            if f is None:
                continue
            yield f
        else:
            temp = {}
            for arg in args:
                f = item.get(arg)
                if f is None:
                    continue
                temp[arg] = f
            if temp != {}:
                yield temp

    # Необходимо реализовать генератор 


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки


def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randrange(begin, end + 1)
