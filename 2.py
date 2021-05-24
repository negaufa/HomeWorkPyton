count_str = 0
count_word = 0
my_dict = {}
with open("task_2.txt", "r") as f:
    for line in f:
        count_str += 1
        count_word = len(line.replace(',', ' ').split(' '))
        my_dict[count_str] = count_word
for i in my_dict:
    print(f'в строке {i} - {my_dict[i]} слов')
