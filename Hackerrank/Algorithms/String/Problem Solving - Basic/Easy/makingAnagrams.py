# Two words are anagrams of one another if their letters can be rearranged to form the other word.

# Given a string, split it into two contiguous substrings of equal length. 
# Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

import math

def makingAnagrams(s1, s2):
    
    first_str = sorted(list(s1))
    last_str = sorted(list(s2))
    
    for i in first_str:
        if i in last_str:
            ind = last_str.index(i)
            last_str.pop(ind)
    
    return len(last_str) * 2

print(makingAnagrams('absdjkvuahdakejfnfauhdsaavasdlkj', 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'))