matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
matrix_2 = [[m[i] for m in matrix] for i in range(len(matrix[1]))]
for line in matrix_2:
    print(line)
