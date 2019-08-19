input_list = list(map(int, input('Введите последовательнось целых чисел через пробел\n').split()))
square_root = []
for a in input_list:
    if a >= 0 and a ** 0.5 % 1 == 0:
        square_root.append(int(a ** 0.5))
print(square_root)
