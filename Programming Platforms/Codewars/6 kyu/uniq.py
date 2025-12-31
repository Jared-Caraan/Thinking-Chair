'''
Implement a function which behaves like the uniq command in UNIX.

It takes as input a sequence and returns a sequence in which all 
duplicate elements following each other have been reduced to one instance.

["a", "a", "b", "b", "c", "a", "b", "c"]  =>  ["a", "b", "c", "a", "b", "c"]
'''

def uniq(seq):
    
    if(len(seq) <= 0):
        return []
    
    ans_seq = []
    
    ans_seq.append(seq[0])
    
    for i in range(1, len(seq)):
        
        if seq[i] != ans_seq[-1]:
            ans_seq.append(seq[i])
    
    return ans_seq

def main():

    lst = [None,'a','a']
    
    print(uniq(lst))

if __name__ == "__main__":
    main()