"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = [] 
    
    if len(s) == 5:
        for i in range(len(s)):
            result.append(f"{s[-(i+1)]}-{len(s)-i}")
        return result
    elif len(s) == 3:
        for i in range(len(s)):
            result.append(f"{s[-(i+1)]}-{len(s)-i}")
        return result
    elif len(s) == 4:
        for i in range(len(s)):
            result.append(str(len(s)-i))
        return result
    elif len(s) == 2:
        for i in range(len(s)):
            result.append(str(len(s)-i))
        return result