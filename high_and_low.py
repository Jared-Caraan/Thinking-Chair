def high_and_low(numbers):
    my_list = numbers.split()
    new_list = list(map(int, my_list))
    new_list.sort()
    
    return str(new_list[-1]) + " " + str(new_list[0])
    
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))