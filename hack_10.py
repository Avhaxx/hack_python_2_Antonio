"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    counter = 1
    for i in s:
        if isinstance(i, dict):
            new_dict = {}
            for k, v in i.items():
                new_dict[str(counter)] = str(counter + 1)
                counter += 2
            result.append(new_dict)
        elif isinstance(i, set):
            new_set = {}
            for k in i:
                new_set[str(counter)] = str(counter + 1)
                counter += 2
            result.append(new_set)
    return result
