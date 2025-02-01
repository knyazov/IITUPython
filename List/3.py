even = []
odd = []
for i in range(0, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

numbers = {"even": even, "odd": odd}
print(numbers["even"])
print(numbers["odd"])
