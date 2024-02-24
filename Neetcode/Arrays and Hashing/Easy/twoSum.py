# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target: int):
        ans = []
        
        for i in range(len(nums)-1, -1, -1):
            if target > 0 and target < nums[i]:
                 continue
            diff = target - nums[i]
            if diff in nums:
                if i != nums.index(diff):
                    ans.append(i)
                    ans.append(nums.index(diff))
                    return ans

print(twoSum([3,3,2,4], 6))

class Solution:
    def twoSum(self, nums: List, target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
