arr = []
for i in range(1, 101):
    temp = []
    if i % 3 == 0:
        temp.append(i)
        arr.append(temp)
print(arr)