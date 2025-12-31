# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:41:52 2019

@author: jcaraan

In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a 
single-digit number is produced. 
This is only applicable to the natural numbers.
"""


def digital_root(n):
    total = 0
    
    for i in str(n):
        total += int(i)
        
    if len(str(total)) <= 1:
        return total
    else:
        return digital_root(total)
    
print(digital_root(493193))