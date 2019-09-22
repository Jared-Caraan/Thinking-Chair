# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:12:08 2019

@author: jcaraan

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

def duplicateCount(string):
    
    string = string.lower()
    holder = []
    count = 0
    
    for i in str(string):
        if i not in holder and ( ((string.rfind(i)) - (string.find(i))) > 0 ):
            holder.append(i)
            count += 1
    
    return count
