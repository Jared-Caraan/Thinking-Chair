'''
Implement a function that receives two IPv4 addresses, 
and returns the number of addresses between them (including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. 
The last address will always be greater than the first one.
'''

from ipaddress import IPv4Address

def solution(start,end):
    
    add1 = int(IPv4Address(start))
    add2 = int(IPv4Address(end))
    
    return add2 - add1

def main():

    print(solution("10.0.0.10","10.0.1.0"))

if __name__ == "__main__":
    main()