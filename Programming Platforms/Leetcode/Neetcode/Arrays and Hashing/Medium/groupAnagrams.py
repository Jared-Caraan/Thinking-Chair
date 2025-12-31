# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
import collections
def groupAnagrams(strs):

    if len(strs) == 0:
        return [[""]]

    if len(strs) == 1:
        return [strs]
    
    holder = []
    anagram_holder = []
    
    for item in strs:
        if sorted(item) in anagram_holder:
            ind = anagram_holder.index(sorted(item))
            holder[ind].append(item)
        else:
            anagram_holder.append(sorted(item))
            holder.append([item])
    
    return holder

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# def groupAnagrams(strs):

#     hash_table = {}
#     for i in range(len(strs)):
#         s = list(strs[i])
#         s.sort()
#         # list is not hashable, so cast it to tuple which is hashable
#         if tuple(s) in hash_table.keys():
#             hash_table[tuple(s)].append(strs[i])
#         else:
#             hash_table[tuple(s)] = [strs[i]]
#     return hash_table.values()

# import collections
# class Solution:
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()
