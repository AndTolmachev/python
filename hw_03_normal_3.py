def my_filter(funk, a):
    b = []
    for i in a:
        if funk(i):
            b.append(i)
        else:
            continue
    return b


z = [1, 2, 3, 4, 5, 6]
print(my_filter(lambda x: x % 2 == 0, z))
