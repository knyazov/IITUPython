def go(numbers):
    list = []
    for number in numbers:
        list.append(
            round(number, 2)
        )
    return tuple(list)

numbers = [3.148, 2.15688, 6.145, 7.893]
print(go(numbers))