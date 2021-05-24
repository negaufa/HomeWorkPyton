rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('task_4.txt', 'r') as f:
    for line in f:
        line = line.split(' ', 1)
        new_file.append(rus[line[0]] + '  ' + line[1])

with open('task_4_new.txt', 'w') as f2:
    f2.writelines(new_file)
