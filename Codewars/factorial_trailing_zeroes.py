def solution(val):

    for i in range(val,0,-1):
        if i % 5 == 0:
            print(i)
            print("Zeroes: " + str(int(i / 5)))
            break;
    
    return 0

def main():
    
    print(solution(30))

if __name__ == "__main__":
	main()