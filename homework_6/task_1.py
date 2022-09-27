# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

inp = list(map(int,input("Insert number: ").split()))
print(list(filter(lambda x:inp.count(x) == 1,inp)))
