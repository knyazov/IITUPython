n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(0)
    matrix.append(row)

num = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(0, m):
            matrix[i][j] = num
            num += 1
    else:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = num
            num += 1
for row in matrix:
    print(row)