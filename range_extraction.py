"""
A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 

The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and 
returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

def solution(args):

    if len(args) == 0:
        return ""
    
    visited = []
    hyph = []
    
    visited.append(args[0])
    
    for i in range(1,len(args)):
        if args[i] - visited[-1] > 1:
            visited.append(args[i])
            if len(hyph) == 2:
                hyph.clear()
            
            if len(hyph) >= 3:
                ind = visited.index(hyph[0])
                del visited[ind:len(hyph) + ind]
                val = "{}-{}".format(str(hyph[0]), str(hyph[-1]))
                visited.insert(ind,val)
                hyph.clear()       
        else:
            if len(hyph) == 0:
                hyph.append(visited[-1])
                hyph.append(args[i])
                visited.append(args[i])
            else:
                hyph.append(args[i])
                visited.append(args[i])
                if args[i] == args[-1]:
                    ind = visited.index(hyph[0])
                    del visited[ind:len(hyph) + ind]
                    val = "{}-{}".format(str(hyph[0]), str(hyph[-1]))
                    visited.append(val)
                    hyph.clear()
    
    str_visited = [str(i) for i in visited]
    res = ",".join(str_visited)
    return res

def main():
    given = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
 
    print(solution(given))
    
if __name__ == "__main__":
    main()