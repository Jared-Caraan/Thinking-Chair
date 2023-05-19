def maxArea(height):
    
    if len(height) == 2:
        return min(height) * 1
    
    max = 0
    sec_max = 0
    width = 0
    area = 0
    dupes = []
    table = {}

    for i in range(len(height)):
        if height[i] > max:
            max = height[i]
        if height[i] in table:
            table[height[i]].append(i)
            if height[i] not in dupes:
                dupes.append(height[i])
                max = 0
        else:
            table[height[i]] = [i]
    
    for i in dupes:
        dupe_area = (i * (table[i][len(table[i])-1] - table[i][0]))
        if dupe_area > area:
            area = dupe_area

    return max
    # max = 0
    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         width = j-i
    #         if height[i] <= height[j]:
    #             length = height[i]
    #         else:
    #             length = height[j]
    #         area = length * width
    #         if area > max:
    #             max = area
    
    # return max


print(maxArea([1,8,6,2,5,4,8,3,7]))