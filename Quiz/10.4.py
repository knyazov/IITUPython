n = 5
pascal = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != i and j != 0:
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    pascal.append(row)

for i in pascal:
    print(i)
