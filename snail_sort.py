def solution(arr):
    
    if len(arr) <= 1:
        return arr
    
    visited = []
    start = base = 0
    counter = len(arr)
    direction = "right"
  
    while(len(visited) != len(arr)**2):
        #print("Hello")
        ## Right
        if direction == "right":
            print(str(start) + " " + str(counter))
            for i in range(start, start + counter):
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
            start = counter - 1
        
        ## Left
        if direction == "left":
            for i in range(start, start - counter, -1):
                visited.append(arr[base][i])
                
                if (i - 1) == (start - counter):
                    base = i
                
            direction = "up"
            counter -= 1
            start = counter
            
        ## Up
        if direction == "up":
            for i in range(start, start - counter, -1):
                visited.append(arr[i][base])
                #print(str(start) + " , " + str(start-counter))
                if (i - 1) == (start - counter):
                    base = i
                    
            direction = "right"
            print("Base: " + str(base))
            
    return visited

def main():

    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    
    print(solution(arr))

if __name__ == "__main__":
	main()