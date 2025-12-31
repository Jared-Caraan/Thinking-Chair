# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(self, nums) -> bool:

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return True
        
        return False

# def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))