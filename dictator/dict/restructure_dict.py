from typing import List, Union


NULL = object()


def restructure_dict(data: Union[List[dict], dict], mapping: dict, extra: dict=None, preserve_others=False) -> \
        Union[dict, List[dict]]:

    if preserve_others:
        restructure_function = __change_keys
    else:
        restructure_function = __clip_data

    if isinstance(data, dict):
        data = restructure_function(data, mapping)
        if extra:
            data.update(extra)
        return data

    else:
        restructured_data = []

        for el in data:
            restructured_data.append(restructure_function(el, mapping))

        if extra:
            for el in restructured_data:
                el.update(extra)

        return restructured_data


def __clip_data(data: dict, mapping: dict) -> dict:

    new_data = {}

    for old_key, new_key in mapping.items():
        value = data.get(old_key)
        new_data[new_key] = value

    return new_data


def __change_keys(data: dict, mapping: dict) -> dict:

    for old_key, new_key in mapping.items():
        value = data.get(old_key, NULL)

        if value != NULL:
            del data[old_key]
            data[new_key] = value

    return data
