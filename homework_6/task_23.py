# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list=[]
# n = int(input("Введите количество элементов списка:"))
# for i in range(n):
#     list.append(int(input(f'Введите элемент {i+1}:')))
# print(list)

# #inp = list(map(float,input('Введите элементы').split()))

# if len(list) % 2 == 1:
#     n1 = len(list) // 2 +1
# else:
#     n1 = len(list)//2
# list1 = []
# for i in range(n1):
#     list1.append(list[i]*list[n-i-1])
    
# print(list1)

inp = list(map(int,input("Insert number: ").split()))
ans = []
for i in range (len(inp)//2):
    ans.append(inp[i]*inp[len(inp)-i-1])
if len(inp) %2 ==1:
    ans.append(inp[int(len(inp)/2)]**2)
print(ans)