from functions import load_json, sort_filter_by_date, format_print

data = load_json('operations.json')

data = sort_filter_by_date(data)

print(format_print(data))

