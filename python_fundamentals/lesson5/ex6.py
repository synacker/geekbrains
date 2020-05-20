import Python_Education_Base.GeekBrains_Python_Base_Work_With_Files_Practice.generators as Generarators
import re
import json

filename = 'ex6.txt'
Generarators.ex6_gen(filename)

result = {}

with open(filename, 'r') as f:
    pattern = re.compile(r"(\w+):\s+(\d+|-).*?(\d+|-).*?(\d+|-)", re.UNICODE)
    for line in f.readlines():
        (name, lesson, practice, labor) = pattern.search(line).groups()
        subject_hours = 0
        for hours in [lesson, practice, labor]:
            try:
                subject_hours += int(hours)
            except ValueError:
                subject_hours += 0
        result[name] = subject_hours

print(json.dumps(result, indent=4, ensure_ascii=False))
