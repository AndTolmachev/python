a = list(map(int, input('Введите последовательность целых чисел через пробел\n').split()))
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] /= 2
    else:
        a[i] *= 2
print(a)
