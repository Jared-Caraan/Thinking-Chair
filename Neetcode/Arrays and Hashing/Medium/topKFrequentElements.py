# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k: int):

        countNums = {}

        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)
        
        countNums = dict(sorted(countNums.items(), key=lambda item: item[1], reverse=True))
        
        return list(countNums.keys())[:k]

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

print(topKFrequent([1,1,1,2,2,3,4,5,5,5,5], 2))