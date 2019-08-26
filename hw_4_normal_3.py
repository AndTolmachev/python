import random

file = open('hw_4_normal_3.txt', 'w')
file.write(''.join([str(random.randint(0, 9)) for _ in range(2500)]))
file.close()
file = open('hw_4_normal_3.txt', 'r', encoding='UTF-8')
char_num = 1
char_max = 1
char_changed = 1
big_int = file.readline()
char = ''
char_m =''
for i in range(1, len(big_int)):
    if big_int[i] == big_int[i-1] and i != len(big_int) - 1:
        char_num += 1
        char = big_int[i]
    else:
        if char_num > char_max:
            char_max = char_num
            char_m = char
        char_num = 1
print(char_m*char_max)
file.close()
