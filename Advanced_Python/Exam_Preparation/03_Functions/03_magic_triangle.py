def get_magic_triangle(number):
    matrix = []

    for i in range(number):
        matrix.append([])
        matrix[i].append(1)
        for j in range(1, i):
            matrix[i].append(matrix[i-1][j-1] + matrix[i-1][j])
        if i != 0:
            matrix[i].append(1)

    print(matrix)
    return matrix


get_magic_triangle(5)
