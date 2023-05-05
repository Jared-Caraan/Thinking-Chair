"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations.In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

Example.


aab shortens to b in one operation: remove the adjacent a characters.


Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.
"""

def superReducedString(s):
    
    flag = False
    
    s = list(s)
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            s[i] = ''
            s[i+1] = ''
            flag = True
            
    s = ''.join(s)
    
    if len(s) == 0:
        return 'Empty String'
    elif flag == False:
        return s
    else:
        return superReducedString(s)
