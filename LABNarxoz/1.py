def sozBarMA(soz, soilem):
    if soz in soilem:
        return True
    return False

matinder = []
for i in range(3):
    matin = input()
    matinder.append(matin)
print("Енгізілген мәтіндер", matinder)
soz = input("Енгізілген сөз ")
indexes = []
for i in range(len(matinder)):
    if sozBarMA(soz, matinder[i]):
        indexes.append(i)
if  len(indexes) != 0:
    print(indexes)