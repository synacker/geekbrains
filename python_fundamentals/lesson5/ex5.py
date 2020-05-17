from random import randint

random_digits = []
for digit in range(0, randint(1, 100)):
    random_digits.append(randint(1, 100000))

filename = 'ex5.txt'
with open(filename, 'w') as f:
    f.write(" ".join(str(digit) for digit in random_digits))

summ = 0
with open(filename, 'r') as f:
    for digit in f.readline().split(" "):
        summ += int(digit)

print(f'Summ - {summ}')

