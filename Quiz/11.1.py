import random

arr = [0] * 10
for i in range(len(arr)):
    arr[i] = random.randint(1, 20)
arr.sort()
arr.reverse()
print(arr)