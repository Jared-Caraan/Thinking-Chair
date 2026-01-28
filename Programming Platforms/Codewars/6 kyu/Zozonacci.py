# n is given as integer and p is given as a list of as abbreviations as strings (e.g. ["fib", "jac", "pad"])
# When n is 0 or p is empty return an empty list.
# The first four elements of the sequence are determined by the first abbreviation in the pattern (see the table below).
# Compute the fifth element using the formula corespoding to the first element of the pattern, the sixth element using the formula for the second element and so on. (see the table below and the examples)
# If n is more than the length of p repeat the pattern.
# zozonacci(["fib", "tri"], 7) == [0, 0, 0, 1, 1, 2, 3]
# a - [0, 0, 0, 1] as "fib" is the first abbreviation
# b - 5th element is 1 as the 1st element of the pattern is "fib": 1 = 0 + 1
# c - 6th element is 2 as the 2nd element of the pattern is "tri": 2 = 0 + 1 + 1
# d - 7th element is 3 as the 3rd element of the pattern is "fib" (see rule no. 5): 3 = 2 + 1

def fib(arr):
    return arr[-1] + arr[-2]

def jac(arr):
    return arr[-1] + (2 * arr[-2])

def pad(arr):
    return arr[-2] + arr[-3]

def pel(arr):
    return (2 * arr[-1]) + arr[-2]

def tet(arr):
    return arr[-1] + arr[-2] + arr[-3] + arr[-4]

def tri(arr):
    return arr[-1] + arr[-2] + arr[-3]

def zozo(pattern, length):

    if len(pattern) == 0 or length == 0:
        return []    
    
    if pattern[0] == "pad":
        holder = [0,1,0,0]
    else:
        holder = [0,0,0,1]
        
    if length <= 4:
        return holder[0:length]
        
    for i in range(0 ,length-4):
        if pattern[i % len(pattern)] == 'fib':
            holder.append(fib(holder))
        elif pattern[i % len(pattern)] == 'jac':
            holder.append(jac(holder))
        elif pattern[i % len(pattern)] == 'pad':
            holder.append(pad(holder))
        elif pattern[i % len(pattern)] == 'pel':
            holder.append(pel(holder))
        elif pattern[i % len(pattern)] == 'tet':
            holder.append(tet(holder))
        elif pattern[i % len(pattern)] == 'tri':
            holder.append(tri(holder))
            
    return holder

print(zozo(["tet"], 10))