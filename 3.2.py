"""Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума)"""

import random
def index(list_, min, max):
    return [i for i in range(len(list_)) if list_[i] <= max and list_[i] >= min]

lst = [random.randint(-20, 20) for i in range(random.randint(10, 30))]
print(lst)
min1 = random.randint(-5, 6)
print(min1)
max1 = random.randint(6, 15)
print(max1)
print ( *index(lst, min1, max1))