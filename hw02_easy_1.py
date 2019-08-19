a = 0
list_of_fruit =[]
while a != '':
    a = input('Напишите название фрукта. Если написали все необзодимые название - нажмите enter\n')
    list_of_fruit.append(a)
max_len = 0
for k in list_of_fruit:
    if max_len < len(k):
        max_len = len(k)
for i, k in enumerate(list_of_fruit):
    if k == '':
        continue
    print(i + 1, '. ', (max_len - len(k))*' ', k, sep='')
