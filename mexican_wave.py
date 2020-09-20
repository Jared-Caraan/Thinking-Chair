def solution(string):
    
    str_list = []
    
    for i in len(string):
        string[i] = string[i].upper()

def main():
    
    test = "test"
    test[0] = test[0].upper()
    
    print(test)


if __name__ == "__main__":
    main()