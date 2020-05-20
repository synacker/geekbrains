import Python_Education_Base.GeekBrains_Python_Base_Work_With_Files_Practice.generators as Generarators
import re
import json

filename = 'ex7.txt'
Generarators.ex7_gen(filename)

result = {}
average_profit = 0
count = 0

with open(filename, 'r') as f:
    pattern = re.compile(r"(\w+|_)\s+(\w+)\s+(\d+)\s+(\d+)", re.UNICODE)
    for line in f.readlines():
        (name, category, profit, lesion) = pattern.search(line).groups()
        count += 1
        profit = int(profit)
        average_profit += profit
        result[name] = profit

if count > 0:
    average_profit /= count

result['average'] = average_profit

with open('ex7.json', 'w') as f:
    print(json.dumps(result, indent=4, ensure_ascii=False), file=f)
