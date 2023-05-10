def divisors(integer):
    arr = [x for x in range(2,integer) if integer % x == 0 ]
    
    if(len(arr) == 0 ):
        return "{} is prime".format(str(integer))
        
    return arr