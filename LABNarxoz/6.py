n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input()))
    matrix.append(row)
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()