# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#list=[]
# n = int(input("Введите количество элементов списка:"))
# for i in range(n):
#     list.append(int(input(f'Введите элемент {i+1}:')))
# print(list)

# sum = 0
# for i in range(n):
#     if i%2 == 1:
#         sum+=list[i]
# print(f'Сумма элементов на нечётных позициях равна {sum}')


inp = list(map(int,input("Insert number: ").split()))
print(sum(list(filter(lambda x:inp.index(x)%2,inp))))

