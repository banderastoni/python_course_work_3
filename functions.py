import json


def sort_by_date(data):
    data.sort(key=lambda x: x['date'], reverse=True)
    return data


def sort_by_state(data):
    data.sort(key=lambda x: x['state'], reverse=True)
    return data


def get_last_5(data):
    return data[:5]


def clear_empty_dict(data):
    for i in range(len(data)):
        if data[i] == {}:
            del data[i]
            break
