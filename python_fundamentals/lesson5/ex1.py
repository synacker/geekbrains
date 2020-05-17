filename = 'ex1.txt'
with open(filename, 'w') as f:
    while True:
        user_input = input()
        if len(user_input) == 0:
            break
        f.write(user_input + '\n')
