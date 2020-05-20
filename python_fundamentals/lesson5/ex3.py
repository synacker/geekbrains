import Python_Education_Base.GeekBrains_Python_Base_Work_With_Files_Practice.generators as Generarators


filename = 'ex3.txt'
base_salary = 20000
Generarators.ex3_gen(filename, salary_base=base_salary)

average_salary = 0
count = 0
with open(filename, 'r') as f:
    for line in f.readlines():
        count += 1
        (name, salary) = line.split()
        salary = int(salary)
        if salary < base_salary:
            print(f'Bad employer - {name}')
        average_salary += salary

if count > 0:
    average_salary /= count

print(f'Average salary - {average_salary}.')