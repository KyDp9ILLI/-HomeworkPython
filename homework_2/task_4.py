# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("Введите число:"))
list=[]
for i in range(n):
    list.append(random.randint(-n,n))
print(list)

num=1
f = open('homework_2/file.txt')
for pos in f:
    if int(pos) < n:
        num*=list[int(pos)]
        print(pos)
    else: num*=1
print(num)