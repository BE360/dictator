
def merge_dict(*args: dict, **kwargs: dict):
    merged_data = {}

    for data in args:
        for k, v in data.items():
            if k not in merged_data:
                merged_data[k].update(v)

    for data_name, data in kwargs.items():
        for k, v in data.items():
            merged_data[k][data_name] = data

    return merged_data
