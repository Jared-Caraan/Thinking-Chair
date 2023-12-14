def banana(input):
    char_dict = {}

    for i in input.upper():
        char_dict[i] = 1 + char_dict.get(i, 0)
    
    b_count = char_dict.get('B', 0) / 1
    a_count = char_dict.get('A', 0) / 3
    n_count = char_dict.get('N', 0) / 2

    return int(min(b_count, a_count, n_count))

def main():
    input = 'QABAAAWOBL'
    print(banana(input))

if __name__ == "__main__":
    main()