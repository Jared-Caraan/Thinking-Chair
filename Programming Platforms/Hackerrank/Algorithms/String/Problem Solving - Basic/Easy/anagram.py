# Two words are anagrams of one another if their letters can be rearranged to form the other word.

# Given a string, split it into two contiguous substrings of equal length. 
# Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

import math

def anagram(s):

    if len(s) % 2 != 0:
        return -1
    
    if sorted(list(s[0: math.floor(len(s)/2)])) == sorted(list(s[math.floor(len(s)/2): len(s)])):
        return 0
    
    first_half = sorted(list(s[0: math.floor(len(s)/2)]))
    last_half = sorted(list(s[math.floor(len(s)/2): len(s)]))
    
    for i in first_half:
        if i in last_half:
            ind = last_half.index(i)
            last_half.pop(ind)
    
    return len(last_half)

print(anagram('abcdbcde'))