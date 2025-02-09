from itertools import permutations
def go(list):
    return permutations(list)

list = [1, 2, 3, 4, 5]
for i in go(list):
    print(i)