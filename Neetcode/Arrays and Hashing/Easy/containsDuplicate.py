def containsDuplicate(self, nums) -> bool:

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                return True
        
        return False