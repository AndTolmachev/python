def sort_to_max(origin_list):
    y = origin_list.copy()
    return_list = []
    for i in range(len(y)):
        a = y.pop()
        for j in range(len(return_list) + 1):
            if j == len(return_list):
                return_list.append(a)
            elif a < return_list[j]:
                return_list.insert(j, a)
                break

    return return_list


z = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(z)
