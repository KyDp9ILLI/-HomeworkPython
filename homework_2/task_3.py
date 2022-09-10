# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Введите число:"))
list = []
for i in range(1,n+1):
    res = round(pow((1+1/i),i),2)
    list.append(res)
print(sum(list))