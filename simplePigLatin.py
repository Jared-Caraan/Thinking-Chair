# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:19:51 2019

@author: jcaraan

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
"""

import string
    
def latin(s):
    holder = s.split()
    val = ""
    
    for i in holder:
        if i in string.punctuation:
            val += i
        else:
             val += i[1:] + i[0] + "ay" + " "
        
    return val