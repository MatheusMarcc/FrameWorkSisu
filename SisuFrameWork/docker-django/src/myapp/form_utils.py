
import re

def parse_nested_fields(flat_data):
    nested_data = {}
    pattern = re.compile(r'^(\w+)\[(\d+)\]\[(\w+)\]$')

    for key, value in flat_data.items():
        match = pattern.match(key)
        if match:
            group, index, subkey = match.groups()
            index = int(index)

            if group not in nested_data:
                nested_data[group] = []

            while len(nested_data[group]) <= index:
                nested_data[group].append({})

            nested_data[group][index][subkey] = value
        else:
            nested_data[key] = value

    return nested_data
