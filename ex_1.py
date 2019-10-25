#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

print([x for x in field(goods, "title")],
      [x for x in field(goods, "title", "price")],
      [x for x in gen_random(0, 3, 5)],
      sep="\n")

# Реализация задания 1
