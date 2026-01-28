'''
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array 
where an uppercase letter is a person standing up.

1. The input string will always be lower case but maybe empty.

2. If the character in the string is whitespace then pass over it as if it was an empty seat.
'''

def wave(people):
    
    str_list = []
    
    for i in range(len(people)):
        ch_list = [ch for ch in people]
        ch_list[i] = ch_list[i].upper()
        
        if ch_list[i] != ' ':
            str_list.append("".join(ch_list))
    
    return str_list

def main():
    
    test = ""
    
    print(wave(test))


if __name__ == "__main__":
    main()