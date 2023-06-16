import json
import datetime
from functions import sort_by_date, sort_by_state, get_last_5

with open('operations.json', 'r', encoding='UTF-8') as f:
    data = json.loads(f.read())

for i in range(len(data)):
    if data[i] == {}:
        del data[i]
        break

#added branch develop

data_sort_by_date = sort_by_date(data)
data_sort_by_state = sort_by_state(data_sort_by_date)
data = get_last_5(data_sort_by_state)

for item in data:
    if "from" in item:
        d = item["date"]
        d = d[:10]
        d = datetime.datetime.strptime(d, '%Y-%m-%d')
        data_split = item["from"].split(' ')
        from_name = ''
        from_number = ''
        if len(data_split) == 3:
            from_name = data_split[0] + ' ' + data_split[1]
            from_number = data_split[2]

        if len(data_split) == 2:
            from_name = data_split[0]
            from_number = data_split[1]

        if from_name == "Счет":
            from_number = '**' + from_number[-4:]
        else:
            from_number = from_number[:4] + ' ' + from_number[4:6] + '** **** ' + from_number[12:]

        data_split = item["to"].split(' ')
        to_name = ''
        to_number = ''
        if len(data_split) == 3:
            to_name = data_split[0] + ' ' + data_split[1]
            to_number = data_split[2]

        if len(data_split) == 2:
            to_name = data_split[0]
            to_number = data_split[1]

        if to_name == "Счет":
            to_number = '**' + to_number[-4:]
        else:
            to_number = to_number[:4] + ' ' + to_number[4:6] + '** **** ' + to_number[12:]

        print('', d.strftime('%d.%m.%Y'), item["description"], '\n',
              from_name, from_number, '->', to_name, to_number, '\n',
              item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"], '\n')
    else:
        d = item["date"]
        d = d[:10]
        d = datetime.datetime.strptime(d, '%Y-%m-%d')

        data_split = item["to"].split(' ')
        to_name = ''
        to_number = ''
        if len(data_split) == 3:
            to_name = data_split[0] + ' ' + data_split[1]
            to_number = data_split[2]

        if len(data_split) == 2:
            to_name = data_split[0]
            to_number = data_split[1]

        if to_name == "Счет":
            to_number = '**' + to_number[-4:]
        else:
            to_number = to_number[:4] + ' ' + to_number[4:6] + '** **** ' + to_number[12:]

        print('', d.strftime('%d.%m.%Y'), item["description"], '\n',
              to_name, to_number, '\n',
              item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"], '\n')
