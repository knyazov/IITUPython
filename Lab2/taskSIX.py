import random

def test_distinct(arr):
    isDistinct = True
    for i in range(len(arr)):
        current = arr[i]
        for j in range(i + 1, len(arr)):
            if current == arr[j]:
                isDistinct = False
                break
    print(f"test_distinct({arr})) = {isDistinct}")

arr = []
for i in range(8):
    arr.append(random.randint(1, 20))
print(arr)
test_distinct(arr)