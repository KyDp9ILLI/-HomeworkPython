# Реализуйте алгоритм перемешивания списка.
import random

list=[]
n = int(input("Введите количество элементов списка"))
for i in range(n):
    list.append(input())
print(list)
i = 1
for i in range(n):
    a = random.randint(0,n-1)
    b = random.randint(0,n-1)
    list[a],list[b] = list[b],list[a]
print(list)


