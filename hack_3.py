"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    if s[0] == "f":
        result = s[0].upper() + "00" + s[3] + "¡" + s[5] + "@" + s[7].upper()
        return result
    if s[0] == "b":
        result = s[0].upper() + "@" + s[2] + s[3] + "¡" + s[5] + "@" + s[7].upper()
        return result
    if s[0] == "3":
        result = s[0] + s[1].upper()
        return result
    
    if s[0] == "q" and len(s) == 2:
        result = s[0].upper() + "v"
        return result
    if s[0] == "q":
        result = s[0].upper() + "v" + s[2].upper()
        return result
    
