import json
import datetime


def load_json(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = json.loads(f.read())
    return data


def sort_filter_by_date(data):
    # синтаксический сахар (генератор списка)
    data_filtered = [item for item in data if item.get("state") == "EXECUTED"]
    # for item in data:
    #     if item.get("state") == "EXECUTED":
    #         data_filtered.append(item)
    data_filtered.sort(key=lambda x: x['date'], reverse=True)

    return data_filtered[:5]


def convert_date(d):
    """Функция конвертирует данные даты из строки в дату"""
    d = d[:10]
    d = datetime.datetime.strptime(d, '%Y-%m-%d')
    d = d.strftime('%d.%m.%Y')
    return d


def mask_card(item):
    """Функция маскирует данные карты и счета"""
    if "from" in item:
        data_split = item.get("from").split(' ')
        # data_split = item["from"].split(' ')
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

        return from_name, from_number, to_name, to_number
    else:
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

        return to_name, to_number


def format_print(data):
    for item in data:
        d = convert_date(item["date"])
        if 'from' in item:
            from_name, from_number, to_name, to_number = mask_card(item)
            print('', d, item["description"], '\n',
                  from_name, from_number, '->', to_name, to_number, '\n',
                  item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"], '\n')
        else:
            to_name, to_number = mask_card(item)
            print('', d, item["description"], '\n',
                  to_name, to_number, '\n',
                  item["operationAmount"]["amount"], item["operationAmount"]["currency"]["name"], '\n')

    return "Success"
