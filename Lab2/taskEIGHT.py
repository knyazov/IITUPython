def sortByHeight(a):
    b = []
    for i in a:
        if i != -1:
            b.append(i)
    b.sort()
    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b[j]
            j += 1
    print(a)


array = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(array)
