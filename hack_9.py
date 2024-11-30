"""
text: {"foo":"fookziman","bar":"barziman"} output =>  {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for key, value in s.items():
        capitalized_key = key.capitalize()
        capitalized_value = value.capitalize().replace("k", "")
        result[capitalized_key] = capitalized_value
        break 
    return result