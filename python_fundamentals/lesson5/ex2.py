import Python_Education_Base.GeekBrains_Python_Base_Work_With_Files_Practice.generators as Generators
import re

filename = 'ex2.txt'
Generators.ex2_gen(filename)

size = 0
words_count = []
with open(filename, 'r') as f:
    for line in f.readlines():
        size += 1
        count = len(re.findall(r"\w+", line))
        words_count.append(count)

print(f'Lines count: {size}.')
print(f'Words count:')

for count in words_count:
    print(f'{count}')
