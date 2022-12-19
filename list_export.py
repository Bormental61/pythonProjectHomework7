def from_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        num_list = data.read()
    return num_list