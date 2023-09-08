"""Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести 
с клавиатуры. Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

def progress(first, step, tot):
    return [first + (i-1) * step for i in range(1, tot + 1)]

frst, stp, tt = int(input()), int(input()), int(input())
print ( * progress(frst, stp, tt))