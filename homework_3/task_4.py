# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input("Введите число:"))

# n=0
# i = 1
# while a // 2 > 0:
#     if a // 2 > 1:
#         n += a % 2*i
#         a//=2
#         i*=10
#     else:
#         n += a % 2*i+ a // 2 *i*10 
#         break

# print(n) 

# num = int(input('Please enter your number: '))

# print(f'{num:b}')

a = int(input('введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)
