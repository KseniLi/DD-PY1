import json

INPUT_FILE = "input_1.csv"

def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    list_dict = []
    list_rows = []
    with open(INPUT_FILE, 'r') as f:
      lis = f.readlines()
      headers = lis[0].rstrip().split(sep=',')
      for row in lis[1:]:
          list_rows.append(row.rstrip().split(sep=','))
    for i in list_rows:
        list_dict.append(dict(zip(headers, i)))
    return list_dict
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
