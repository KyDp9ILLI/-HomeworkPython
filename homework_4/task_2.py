#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number=int(input("Введите число:"))
list1 = []

for i in range(2, number): 
    while (number % i == 0): 
        list1.append(i)
        number //= i 

if (number != 1): 
    list1.append(number)

print(list1)