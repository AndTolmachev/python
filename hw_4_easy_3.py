import random

list_int = [random.randint(10, 100) for _ in range(20)]
list_res = [l_i for l_i in list_int if l_i > 0 and l_i % 3 == 0 and l_i % 4 != 0]
print(list_res)
