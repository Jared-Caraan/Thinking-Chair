# There is a collection of rocks where each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range ascii[a-z]. There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.

# Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.

# Example arr = ['abc','abc','bc']

# The minerals b and c appear in each rock, so there are 2 gemstones.

def gemstones(arr):
    dict = {}
    count = 0
    for ind, ele in enumerate(arr):
        for j in ele:
            if j in dict.keys():
                dict[j].add(ind)
            else:
                dict[j] = {ind}
    
    for i in dict.values():
        if set(range(0,len(arr))) == i:
            count += 1

    return count

print(gemstones(['abcdde', 'baccd', 'eeabg']))

def gemstones(arr):
    gems = {}
    for i in range(len(arr)):
        if(i==0):
          gems = set(arr[i])
        else:
            gems = gems & set(arr[i]) 
    return (len(gems)) 