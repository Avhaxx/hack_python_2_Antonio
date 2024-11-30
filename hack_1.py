"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    if len(s) > 3:
        result = s[0] + s[1].upper() + s[2] + s[3] + s[4].upper() + s[5:]
        return result
    if len(s) == 3:
        result = s[0] + s[1].upper() + s[2]
        return result
    else:
        result = s
        return result
    