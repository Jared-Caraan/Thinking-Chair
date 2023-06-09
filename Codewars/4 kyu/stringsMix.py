# Given two strings s1 and s2, we want to visualize how different the two strings are. 
# We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

# s1 = "A aaaa bb c"

# s2 = "& aaa bbb c d"

# s1 has 4 'a', 2 'b', 1 'c'

# s2 has 3 'a', 3 'b', 1 'c', 1 'd'

# So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. 
# In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

# We can resume the differences between s1 and s2 in the following string: 
# "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. 
# In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

# The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if 
# this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with 
# their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

# In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in 
# decreasing order of their length and when they have the same length sorted in 
# ascending lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'.

def stringsMix(s1,s2):
    
    # holder = []
    # countS1 = {}
    # countS2 = {}
    # res = ""

    # for i in s1:
    #     if 97 <= ord(i) and ord(i) <= 122:
    #         if i not in countS1:
    #             countS1[i] = "1:" + i
    #         else:
    #             countS1[i] = countS1.get(i,"") + i

    # for i in s2:
    #     if 97 <= ord(i) and ord(i) <= 122:
    #         if i not in countS2:
    #             countS2[i] = "2:" + i
    #         else:
    #             countS2[i] = countS2.get(i,"") + i
    
    # for i in countS1.items():
        
    #     if i[0] in countS2:
    #         if (len(countS2[i[0]]) > len(i[1])) and len(countS2[i[0]]) > 3:
    #             holder.append((countS2[i[0]][2], countS2[i[0]]))
    #         elif len(countS2[i[0]]) == len(i[1]) and (len(countS2[i[0]]) > 3 or len(i[1]) > 3):
    #             countS2[i[0]] = "=" + countS2[i[0]][1:]
    #             holder.append((countS2[i[0]][2], countS2[i[0]]))
    #         elif (len(countS2[i[0]]) < len(i[1])) and len(i[1]) > 3:
    #             holder.append(i)
    #     elif i[0] not in countS2 and len(i[1]) > 3:
    #         holder.append(i)
    
    # for i in countS2.items():
    #     if i[0] not in countS1 and len(i[1]) > 3:
    #         holder.append(i) 
    
    # holder = sorted(sorted(sorted(holder, key= lambda e: ord(e[0])), key= lambda e: e[1][0]), key= lambda e: len(e[1]), reverse=True)

    # for i in range(len(holder)):
    #     res += holder[i][1]
    #     if i != len(holder)-1:
    #         res += "/"
    # return res

    s = []
    lett = "abcdefghijklmnopqrstuvwxyz"
    for ch in lett:
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) >= 2:
            if val1 > val2: s.append("1:"+val1*ch)
            elif val1 < val2: s.append("2:"+val2*ch)
            else: s.append("=:"+val1*ch)
            
    s.sort()
    s.sort(key=len, reverse=True)
    return "/".join(s)

print(stringsMix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))