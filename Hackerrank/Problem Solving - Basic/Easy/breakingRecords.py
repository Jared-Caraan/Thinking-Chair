# Given the scores for a season, determine the number of times Maria breaks her records 
# for most and least points scored during the season.

# Input: 10 5 20 20 4 5 2 25 1
# Output: 2 4

def breakingRecords(scores):
    if len(scores) == 1:
        return [0,0]
    
    max_points, min_points = 0,0
    max_counter = 0
    min_counter = 0

    for i in range(0,len(scores)):
        if i == 0:
            max_points, min_points = scores[i],scores[i]
        else:
            if scores[i] > max_points:
                max_counter += 1
                max_points = scores[i]
            if scores[i] < min_points:
                min_counter += 1
                min_points = scores[i]
    
    return [max_counter, min_counter]