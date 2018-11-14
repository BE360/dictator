from typing import Union


def list_to_dict(data_list: list, keys: Union[str, tuple], distinct=True) -> dict:
    data_dict = {}

    for data in data_list:
        if isinstance(keys, str):
            _key = data.get(keys)
        else:
            _key = tuple(data.get(k) for k in keys)

        _val = data

        if distinct:
            data_dict[_key] = _val
        else:
            if _key not in data_dict:
                data_dict[_key] = [_val]
            else:
                data_dict[_key].append(_val)

    return data_dict
