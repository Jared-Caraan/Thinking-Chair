# Given an integer array nums, return an array answer such that answer[i] is equal 
# to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):

    left_products = [1] * len(nums)
    right_products = [1] * len(nums)

    for i in range(1, len(nums)):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    # [1,1,2,6]

    for i in range(len(nums) - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    # [24,12,4,1]

    product_of_array_excluding_self = [
        left_products[i] * right_products[i] for i in range(len(nums))
    ]
    # [24,12,8,6]

    return product_of_array_excluding_self

    

print(productExceptSelf([1,2,3,4]))

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res
