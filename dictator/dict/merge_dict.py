
def merge_dict(*args: dict, **kwargs):
    merged_data = {}

    for data in args:
        for k, v in data.items():
            merged_data[k] = v

    for data_name, data in kwargs.items():
        merged_data[data_name] = data

    return merged_data
