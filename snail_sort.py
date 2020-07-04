def solution(arr):
    
    if len(arr) <= 1:
        return arr
    
    visited = []
    start = 0
    iter = 0
    base = 0
    counter = len(arr)
    direction = "right"
  
    while(len(visited) != len(arr)**2):
        
        ## Right
        if direction == "right":
            for i in range(start + iter, start + counter + iter):
                visited.append(arr[base][i])
                
                if (i + 1) == (start + counter):
                    base = i
                    
            direction = "down"
            start += 1
            counter -= 1
        
        ## Down
        if direction == "down":
            for i in range(start, start + counter):
                visited.append(arr[i][base])
              
                if (i + 1) == (start + counter):
                    base = i
                    
            direction = "left"
            start = (len(arr) - 2) - iter
        
        ## Left
        if direction == "left":
            for i in range(start, start - counter, -1):
                visited.append(arr[base][i])
                
                if (i - 1) == (start - counter):
                    base = i
                
            direction = "up"
            counter -= 1
            
        ## Up
        if direction == "up":
            #print(str(start) + " - " + str((start - counter)))
            for i in range(start, (start - counter), -1):
                visited.append(arr[i][base])
            
                if (i - 1) == (start - counter):
                    base = i
                    
            direction = "right"
            start = 0
            iter += 1
        
    return visited

def main():

    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] 
    arr2 = [[1,2,3],[4,5,6],[7,8,9]]
    
    print(solution(arr))
    
if __name__ == "__main__":
	main()