# Given an array of bird sightings where every element represents a bird type id, 
# determine the id of the most frequently sighted type. 
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

# arr = [1,1,2,2,3]
# There are two each of types 1 and 2, and one sighting of type 3. 
# Pick the lower of the two types seen twice: type 1.

from collections import Counter

def migratoryBirds(arr):

    holder = []
    max = 1
    
    multiset = Counter(arr).most_common()

    for i in multiset:
        if i[1] >= max:
            max = i[1]
            holder.append(i[0])
    
    return min(holder)

print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))