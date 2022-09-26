#Вычислить число пи c заданной точностью d

a = int(input("Введите количество знаков после запятой в числе pi "))

k=1
sum=0
for i in range (1000000):
    if i % 2 == 0:
        sum+=4/k
    else:
        sum-=4/k
    k+=2
print(round(sum,a))