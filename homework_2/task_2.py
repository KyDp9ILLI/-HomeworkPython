# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#  пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

a = int(input("Введите число:"))
list = []
for i in range(1,a+1):
    if i==1:
        list.append(1)
    else:
        res=1     
        while i>1:
            #print(res)
            res*=i
            #print(res)
            i-=1
        list.append(res)
print(list)
