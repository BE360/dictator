from typing import List, Union


def sum_dict(data: List[dict], keys: list, key_postfix: str='_sum'):

    result = {}

    for k in keys:
        key = k + key_postfix
        value = sum([d[k] for d in data])

        result[key] = value

    return result
