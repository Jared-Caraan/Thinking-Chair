# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

from itertools import product
import math

def generateParenthesis(n: int):
    holder = {1: ["()"], 2: ["(())", "()()"]}
    if n == 1 or n == 2: return holder[n]

    new_key_values = {i: set() for i in range(3,n+1)}
    holder.update(new_key_values)
    counter = 3
    catalan = int(math.factorial(2 * n) / (math.factorial(n + 1) * math.factorial(n)))

    while len(holder[n]) != catalan: 
        for i in range(1, counter-1):
            lst = holder[i]
            lst2 = holder[counter-i]
            prod = list(product(lst, lst2))
            prod2 = list(product(lst2, lst))

            for i in prod:
                pattern = i[0] + i[1]
                if pattern not in holder[counter]:
                    holder[counter].add(pattern)

            if prod2 != prod:        
                for j in prod2:
                    pattern = j[0] + j[1]
                    if pattern not in holder[counter]:
                        holder[counter].add(pattern)
        
        if len(holder[counter-1]) != 0:
            prev = holder[counter-1]
            for i in prev:
                pattern = '(' + i + ')'
                if pattern not in holder[counter]:
                    holder[counter].add(pattern)
        
        counter += 1

    return sorted(list(holder[n]))

print(generateParenthesis(8))

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()
#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res
