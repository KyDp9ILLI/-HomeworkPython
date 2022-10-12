# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list=[]
# n = int(input("Введите количество элементов списка:"))
# for i in range(n):
#     list.append(float(input(f'Введите элемент {i+1}:')))
# print(list)

# max = list[0] - int(list[0])
# min = list[0] - int(list[0])

# for i in range(n):мм
#     if list[i]-int(list[i]) > max:
#         max = list[i]-int(list[i])
#     elif list[i]-int(list[i]) < min:
#         min = list[i]-int(list[i])

# print(round(max-min,2))


res = map(float,input("Введите числа: ").split())
res = list(map(lambda x: x - int(x),res))
print(round(max(res)-min(res),2))