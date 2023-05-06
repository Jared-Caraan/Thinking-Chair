# In this challenge, you will determine whether a string is funny or not. 
# To determine whether a string is funny, create a copy of the string in reverse e.g. abc -> cba. 
# Iterating through each string, compare the absolute difference in the ascii values of the characters at 
# positions 0 and 1, 1 and 2 and so on to the end. 
# If the list of absolute differences is the same for both strings, they are funny.

# Determine whether a give string is funny. If it is, return Funny, otherwise return Not Funny.

def funnyString(s):

    holder_forward = []
    holder_rev = []

    string_list = list(s)
    ascii_list = [ord(i) for i in string_list]

    string_list_rev = string_list[::-1]
    ascii_rev = [ord(i) for i in string_list_rev]

    for i in range(0, len(ascii_list)-1):
        holder_forward.append(abs(ascii_list[i] - ascii_list[i+1]))
        holder_rev.append(abs(ascii_rev[i] - ascii_rev[i+1]))
    
    if holder_forward == holder_rev:
        return 'Funny'
    
    return 'Not Funny'
