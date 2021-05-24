firms = []
firm = {}
profit_firms = []
count = 0
average_profit = 0
profit_firms_dict = {}
none_profit_firm_dict = {}
none_profit_firm = []
profit_firm = []
with open('task_7.txt', 'r') as f:
    for line in f:
        line = line.split(' ')
        firm = {'firm_name': line[0], 'type_of_ownership': line[1], 'proceeds': line[2], 'costs': line[3][:-1],
                'profit': int(line[2]) - int(line[3][:-1])}
        firms.append(firm)
print(firms)
print('-' * 15)

for i in firms:
    if i['profit'] > 0:
        count += 1
        average_profit += i['profit']
        profit_firms_dict[i['firm_name']] = i['profit']

    else:
        none_profit_firm_dict[i['firm_name']] = i['profit']
    average_profit = average_profit / count

profit_firm.append(profit_firms_dict)
none_profit_firm.append(none_profit_firm_dict)

profit_firms.append(profit_firm)
profit_firms.append(none_profit_firm)
print(profit_firms_dict)
print(profit_firms)
