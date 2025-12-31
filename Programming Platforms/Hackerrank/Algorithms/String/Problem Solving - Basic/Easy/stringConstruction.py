# Amanda has a string of lowercase letters that she wants to copy to a new string. 
# She can perform the following operations with the given costs. 
# She can perform them any number of times to construct a new string p:

# Append a character to the end of string p at a cost of 1 dollar.
# Choose any substring of p and append it to the end of p at no charge.
# Given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

# For example, given a string s=abcabc, it can be copied for 3 dollars. 
# Start by copying a, b and c individually at a cost of 1 dollar per character. 
# String p = abc at this time. Copy p[0:2] to the end of p at no cost to complete the copy.

def stringConstruction(s):

    if len(s) == 1:
        return 1
    
    holder = ""
    price = 0
    
    for i in s:
        if i not in holder:
            holder += i
            price +=1
    
    return price


print(stringConstruction('abba'))