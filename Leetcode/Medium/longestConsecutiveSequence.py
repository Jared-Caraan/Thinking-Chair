# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    max = 0
    counter = 0
    nums = sorted(list(set(nums)))

    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 1:
            counter += 1
            if max < counter:
                max = counter
        else:
            counter = 0

    return max + 1
    # return nums

print(longestConsecutive([1,2,0,1]))

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for n in nums:
#             # check if its the start of a sequence
#             if (n - 1) not in numSet:
#                 length = 1
#                 while (n + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest
