print("Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")

print("Введите число")
a = int(input())

if a == 1 or a == 2 or a == 3 or a == 4 or a == 5:
    print("Не является выходным")
elif a == 6 or a == 7 :
    print("Является выходныи")
else :
    print ("Некоректно введены данные")