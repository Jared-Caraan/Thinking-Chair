def weightedUniformStrings(s, queries):
    holder = []
    counter = 1

    for i in range(len(s)):
        if i != 0 and s[i-1] == s[i]:
            counter += 1
            holder.append((ord(s[i]) - 96 ) * counter)
        else:
            counter = 1
            holder.append(ord(s[i]) - 96)

    return ['Yes' if i in holder else 'No' for i in queries]

print(weightedUniformStrings('aaabbbbcccddd', [6,1,3,12,5,9,10]))