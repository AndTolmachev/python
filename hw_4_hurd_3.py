import random

quins = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 5), (3, 5), (4, 6)]
under_attack = 'NO'
for i in range(7):
    for j in range(i+1, 8):
        if quins[i][0] == quins[j][0] or quins[i][1] == quins[j][1] or \
            quins[i][0] + quins[i][1] == quins[j][0] + quins[j][1] or \
                quins[i][0] - quins[i][1] == quins[j][0] - quins[j][1]:
            under_attack = 'YES'
print(under_attack)
