def solution2(pattern, length):
    
    if len(pattern) == 0 or length == 0:
        return []    
    
    if pattern[0] == "pad":
        holder = [0,1,0,0]
    else:
        holder = [0,0,0,1]
        
    if length <= 4:
        return holder[0:length]
        
    if len(pattern) <= length:
        pattern = pattern*length
        for i in range(0, length-4):
            if pattern[i] == "fib":
                holder.append(holder[-1] + holder[-2])
            elif pattern[i] == "jac":
                holder.append(holder[-1] + 2 * holder[-2])
            elif pattern[i] == "pad":
                holder.append(holder[-2] + holder[-3])
            elif pattern[i] == "pel":
                holder.append(2 * holder[-1] + holder[-2])
            elif pattern[i] == "tet":
                holder.append(holder[-1] + holder[-2] + holder[-3] + holder[-4])
            elif pattern[i] == "tri":
                holder.append(holder[-1] + holder[-2] + holder[-3])
    else:
        for i in range(1, length-3):
            if pattern[i] == "fib":
                holder.append(holder[-1] + holder[-2])
            elif pattern[i] == "jac":
                holder.append(holder[-1] + 2 * holder[-2])
            elif pattern[i] == "pad":
                holder.append(holder[-2] + holder[-3])
            elif pattern[i] == "pel":
                holder.append(2 * holder[-1] + holder[-2])
            elif pattern[i] == "tet":
                holder.append(holder[-1] + holder[-2] + holder[-3] + holder[-4])
            elif pattern[i] == "tri":
                holder.append(holder[-1] + holder[-2] + holder[-3])
            
    return holder
        
def main():

    holder = [1,2,3]
    
    for i in range(0,5):
        holder.append(holder[-1] + holder[-1])
    print(holder)
    #print(solution2(["pad", "tri"], 5))
    
if __name__ == "__main__":
	main()