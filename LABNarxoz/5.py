n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
tanba = input()
if tanba == '+':
    numbers = [numbers[-1]] + numbers[0:-1]
elif tanba == '-':
    numbers = numbers[1:] + [numbers[0]]
for i in numbers:
    print(i, end=" ")