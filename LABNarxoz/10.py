def union(set1, set2):
    result = set1.copy()
    for i in set2:
        result.add(i)
    return result


def intersection(set1, set2):
    result = set()
    for element in set1:
        if element in set2:
            result.add(element)
    return result


def diff(set1, set2):
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    return result


set1 = {1, 2, 3}
set2 = {4, 5, 2}
print(union(set1, set2))
print(intersection(set1, set2))
print(diff(set1, set2))
