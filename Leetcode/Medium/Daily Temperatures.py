# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    stack = []
    res = [0 for i in range(len(temperatures))]
    index = {i: [] for i in temperatures}

    for i in range(len(temperatures)-1, -1, -1):
        if len(stack) != 0:
            while len(stack) != 0 and temperatures[i] >= stack[-1]:
                stack.pop()
            if len(stack) != 0:
                res[i] = index[stack[-1]][-1] - i
            stack.append(temperatures[i])
            index[temperatures[i]].append(i)
            continue
        stack.append(temperatures[i])
        index[temperatures[i]].append(i)
    
    return res

print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []  # pair: [temp, index]

#         for i, t in enumerate(temperatures):
#             while stack and t > stack[-1][0]:
#                 stackT, stackInd = stack.pop()
#                 res[stackInd] = i - stackInd
#             stack.append((t, i))
#         return res
