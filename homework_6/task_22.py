# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list1 = []
# n = int(input("Введите количесвто элементов списка: "))
# for i in range (n):
#     list1.append(int(input("Введите элемент списка: ")))

# new_list = []

# for x in list1:
#     if x not in new_list:
#         new_list.append(x)

# print(f'Первоначальная последовательность чисел {list1}')
# print(f'Изменённая последовательность чисел {new_list}')

print(set(list(map(int,input("Insert number: ").split()))))