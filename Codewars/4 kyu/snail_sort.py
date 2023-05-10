"""
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
"""

def solution(snail_map):
    
    visited = []
    start = 0
    iter = 0
    base = 0
    counter = len(snail_map)
    direction = "right"
    
    if len(snail_map[0]) == 0:
        return visited
  
    while(len(visited) != len(snail_map)**2):
        
        ## Right
        if direction == "right":
            for i in range(start + iter, start + counter + iter):
                visited.append(snail_map[base][i])
                
                if (i + 1) == (start + counter + iter):
                    base = i
                    
            direction = "down"
            start += 1
            counter -= 1
        
        ## Down
        if direction == "down":
            for i in range(start + iter, start + counter + iter):
                visited.append(snail_map[i][base])
                
                if (i + 1) == (start + counter + iter):
                    base = i
                    
            direction = "left"
            start = (len(snail_map) - 2) - iter
        
        ## Left
        if direction == "left":
            for i in range(start, start - counter, -1):
                visited.append(snail_map[base][i])
                
                if (i - 1) == (start - counter):
                    base = i
                
            direction = "up"
            counter -= 1
            
        ## Up
        if direction == "up":
            for i in range(start, (start - counter), -1):
                visited.append(snail_map[i][base])
                
                if (i - 1) == (start - counter):
                    base = i
                    
            direction = "right"
            start = 0
            iter += 1
        
    return visited

def main():

    snail_map = [[]]
    
    print(solution(snail_map))
    
if __name__ == "__main__":
	main()