user_text = input('Введите текст').split()
with open("task_1.txt", 'w') as f:
    for line in user_text:
        f.write(line + '\n')

