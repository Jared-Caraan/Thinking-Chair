def groupAnagrams(strs):

    if len(strs) == 0:
        return [[""]]

    if len(strs) == 1:
        return [strs]
    
    holder = []
    anagram_holder = {}
    
    for index, item in enumerate(strs):
        if sorted(item) in anagram_holder:
            ind = anagram_holder[sorted(item)]
            holder[ind].append(item)
        anagram_holder[sorted(item)] = index
        holder.append([item])
    
    return holder