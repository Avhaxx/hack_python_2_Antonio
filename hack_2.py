"""
generic script

text: "fooziman" output => "fzmn" 
       01234567
text: "barziman" output => "brzmn" 
       01234567
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    
    if s[0] == "f":
        result = s[0] + s[3] + s[5] + s[7]
        return result
    
    if s[0] == "b":
        result = s[0] + s[2] + s[3] + s[5] + s[7]
        return result
    else:
        result = s[0] + s[2] 
        return result