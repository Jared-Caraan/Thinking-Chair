# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
def searchInsert(nums, target: int):
    if target in nums:
        return nums.index(target)
    
    if target > nums[len(nums)-1]:
        return len(nums)
    
    if nums[0] > target:
        return 0
    
    ans = 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if target < nums[middle]:
            if middle - 1 <= left:
                ans = middle
            right = middle - 1
        elif target > nums[middle]:
            if middle + 1 >= right:
                ans = middle + 1
            left = middle + 1
    return ans

    # l, r = 0, len(nums)-1
    # while l <= r:
    #     mid = (r + l) // 2
    #     if target <= nums[mid]:
    #         r = mid - 1
    #     elif target >= nums[mid]:
    #         l = mid + 1
    #     else:
    #         return mid
    # return l

print(searchInsert(nums = [1,3,5], target = 4))