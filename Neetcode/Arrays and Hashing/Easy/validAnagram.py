# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

def isAnagram(self, s: str, t: str) -> bool:

        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t

# def isAnagram(s,t):
#     if len(s) != len(t):
#         return False
    
#     countS, countT = {},{}

#     # create hashmap for each letter as key, and their count as value
#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countS[t[i]] = 1 + countS.get(t[i], 0)
    
#     # compare the count of letter of two hashmaps
#     for c in countS:
#         if countS[c] != countT.get(c,0):
#             return False
#     return True

# from collections import Counter
# def isAnagram(s,t):
#     return Counter(s) == Counter(t)