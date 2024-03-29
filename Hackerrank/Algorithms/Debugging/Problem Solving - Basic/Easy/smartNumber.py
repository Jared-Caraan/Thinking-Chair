# A number is called a smart number if it has an odd number of factors. 
# Given some numbers, find whether they are smart numbers or not.

# Debug the given function is_smart_number to correctly check if a given number is a smart number.

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

print(is_smart_number(169))