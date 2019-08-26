def input_list(text):
    return input(text).split()


fruit_list_1 = input_list('Введите список фруктов через пробел\n')
fruit_list_2 = input_list('Введите второй список фруктов через пробел\n')
fruit_list_coincedense = [f_l for f_l in fruit_list_1 if f_l in fruit_list_2]
print(fruit_list_coincedense)
