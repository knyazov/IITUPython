def barMa(soz, soilem):
    return soz in soilem


def toltyr(txt):
    matinder = []
    while True:
        print(f"[1] {txt} енгізіңіз")
        print("[0] Болды, токтаймыз")
        choice = int(input())
        if choice == 1:
            soilem = input()
            matinder.append(soilem)
        elif choice == 0:
            break
    return matinder


result = {}
matinder, sozder = [], []

matinder = toltyr("Сөлем")
sozder = toltyr("Сөздер")
print("Енгізілген мәтіндер: ", matinder)
print("Енгізілген сөздер: ", sozder)
for soz in sozder:
    indexes = []
    for i in range(len(matinder)):
        if barMa(soz, matinder[i]):
            indexes.append(i)
    result[soz] = indexes
print(result)