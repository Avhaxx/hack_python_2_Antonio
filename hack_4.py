"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    if s[0] == "f":
        result = s[1:7] 
        return result
    
    if s[0] == "b":
        result = s[1:7]
        return result
    
    if s[0] == "q":
        result = s
        return result
    
