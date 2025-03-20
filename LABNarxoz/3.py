pander = {
    "Math" : 70,
    "Bio" : 80,
    "Phys" : 55,
    "DW" : 100
}

def tauypBer():
    result = ""
    min = 150
    for key, value in pander.items():
        if value < min:
            min = value
            result = key
    return result

print(tauypBer())