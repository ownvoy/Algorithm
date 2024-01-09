n = int(input())
matrix = [list(input().strip()) for _ in range(n)]


def check_max_sequence(matrixx):
    max_sequence = 0
    for row in matrixx:
        temp = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                temp += 1
                max_sequence = max(max_sequence, temp)
            else:
                temp = 1
    return max_sequence


def find(matrixx):
    maxx_row = check_max_sequence(matrixx)
    transposed_matrix = zip(*matrixx)
    maxx_col = check_max_sequence(transposed_matrix)
    maxx = max(maxx_row, maxx_col)
    return maxx


maxx = 0
for i in range(n):
    for j in range(n - 1):
        if matrix[i][j] != matrix[i][j + 1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            maxx = max(maxx, find(matrix))
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

for i in range(n - 1):
    for j in range(n):
        if matrix[i][j] != matrix[i + 1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            maxx = max(maxx, find(matrix))
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]

print(maxx)
