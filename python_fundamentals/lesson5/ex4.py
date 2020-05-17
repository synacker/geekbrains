from num2words import num2words
import Python_Education_Base.GeekBrains_Python_Base_Work_With_Files_Practice.generators as Generarators
import re

filename = 'ex4.txt'
Generarators.ex4_gen(filename, 1000)

with open(filename, 'r') as f:
    pattern = re.compile(r"(.+)-(\d+)", re.UNICODE)
    for line in f.readlines():
        (name, digit) = pattern.search(line).groups()
        digit = int(digit)
        print(f'{num2words(digit, lang="ru")}-{digit}')