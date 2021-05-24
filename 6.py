subjects = {}

with open('task_6.txt', 'r') as f:
    for line in f.readlines():
        data = line.replace('(', ' ').split()
        subjects[data[0]] = sum(
            int(i) for i in data if i.isdigit()
        )

print(subjects)
