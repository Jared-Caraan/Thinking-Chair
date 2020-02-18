def generate_hashtag(val):
    if len(val) == 0 or len(val) >= 140:
        return False
        
    list = val.split()
    upper_list = [x[0].upper() + x[1:].lower() for x in list]
    res = ''.join(upper_list)
    
    return '#' + res

def main():
    res = generate_hashtag("")
    print(len(res))

if __name__ == "__main__":
    main()