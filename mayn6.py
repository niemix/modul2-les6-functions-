def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        mat = []
        for j in range(m):
            mat.append(value)
        matrix.append(mat)
    return matrix
result1 = get_matrix(4, 1, 73)
result2 = get_matrix(3, 4, 42)
result3 = get_matrix(3, 3, 666)
print(result1)
print(result2)
print(result3)



