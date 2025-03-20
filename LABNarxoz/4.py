panderDictionary = {
    "Math": 70,
    "Bio": 80,
    "Phys": 55,
    "DW": 100,
    "History": 94
}

pander = []
for key, value in panderDictionary.items():
    panKortej = (key, value)
    pander.append(panKortej)
n = len(pander)
for i in range(n):
    for j in range(0, n - i - 1):
        if pander[j][1] < pander[j + 1][1]:
            pander[j], pander[j + 1] = pander[j + 1], pander[j]

sortedDictionary = {}
for kye, value in pander:
    sortedDictionary[kye] = value
print(sortedDictionary)
