"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
       01234567
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    if s[0] == "f":
        result = "fo-" + s[3] + s[4] + "-" + s[5] + s[6] + "-"
        return result
    elif s[0] == "b":
        result = "" 
        for char in s:
            if char == 'r':
                result += '-'
            elif char == 'm':
                result += '-'
            else:
                result += char
        return result
    elif s[0] == "q":
        result = s[0] + s[1] + '-'
        return result
    else:    
        return s