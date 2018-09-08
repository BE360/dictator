from typing import List


def sum_dict(data: List[dict], keys: tuple):
    relation_notation = '__'

    results = {}

    for key in keys:
        if relation_notation not in key:
            value = sum([d.get(key, 0) for d in data])
            results[key] = value

        else:
            key_parts = key.split(relation_notation)
            sum_key = key_parts[-1]

            data_element = data
            result_element = results

            for rel_key in key_parts[:-1]:
                if rel_key not in result_element:
                    result_element[rel_key] = {}

                result_element = result_element[rel_key]
                data_element = data_element.get(rel_key, {})

            value = sum([d.get(sum_key, 0) for d in data_element])
            result_element[sum_key] = value

    return results
