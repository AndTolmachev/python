list_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'd', 'e', 'f', 'g',]
list_two = ['e', 'f', 'g', 'h', 'x', 'z', 'y']
index_list_one = []
set_one_two = set(list_one).intersection(list_two)
for i, k in enumerate(list_one):
    if k in set_one_two:
        index_list_one = [i] + index_list_one
for j in index_list_one:
    list_one.pop(j)
print(list_one)
