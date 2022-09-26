# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input("Введите число:"))

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

list = []
for i in range(1,a+1):
    list.insert(0,(pow(-1,i+1)*fib(i)))
    list.append(fib(i))
list.insert(a,0)
print(list)
