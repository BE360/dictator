
def merge_dict(*data_list: dict):
    merged_data = {}

    for data in data_list:
        for k, v in data.items():
            merged_data[k] = v

    return merged_data
