import random

n = int(input('Введите количество элементов в списке\n'))
rand_list =[]
for i in range(n):
    rand_list.append(random.randint(-100, 100))
print(rand_list)
