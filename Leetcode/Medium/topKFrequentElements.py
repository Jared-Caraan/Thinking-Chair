# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k: int):

        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)
        
        countNums = dict(sorted(countNums.items(), key=lambda item: item[1], reverse=True))
        
        return list(countNums.keys())[:k]

print(topKFrequent([1,1,1,2,2,3,4,5,5,5,5], 2))