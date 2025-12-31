def main(arr):

    res = []
    current = []
    
    def backtrack(nums):

        # stopping condition
        if len(current) == len(nums):
            res.append(current)
            return
        
        # start from the first element
        for i in nums:
            if i in current:
                continue
            current.append(i)
            backtrack(nums)
            current.pop()

    backtrack(arr)

    return res

# def money_changer(moneys, change):

#     res = []
#     multiplier = 1

#     def backtrack(moneys, change):

#         if change == 0:
#             return res
#         for i in range(len(moneys)-1, -1, -1):
#             if change >= moneys[i]:
#                 res.append([moneys[i]])
#                 backtrack(moneys[i], change)
#                 res.pop()
    
#     for i in range(len(moneys)-1, -1, -1):
#         if change >= moneys[i]:
#             mult = change // moneys[i]
#             while mult != 0:
#                 moneys[i] = mult * moneys[i]

#     return res

# print(money_changer([2, 4, 5, 7, 8, 9], 19))
print(main([1,2,3]))