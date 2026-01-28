# An array is defined to be odd-heavy if it contains at least one odd element and 
# every element whose value is odd is greater than every even-valued element.

# Array [11,4,9,2,8] is odd-heavy,
# because its odd elements [11,9] are greater than all the even elements [4,2,8]

# Array [11,4,9,2,3,10] is not odd-heavy,
# because one of its even elements (10 from [4,2,10]) is greater than two of
# its odd elements (9 and 3 from [11,9,3])

# Array [] is not odd-heavy,
# because it does not contain any odd numbers

# Array [3] is odd-heavy,
# because it does not contain any even numbers.

def is_odd_heavy(arr):
    odd_arr = [i for i in arr if i % 2 != 0 ]
    even_arr = [i for i in arr if i % 2 == 0 ]

    if not odd_arr:
        return False
    
    if not even_arr:
        return True
    
    max_even = max(even_arr)

    for i in odd_arr:
        if max_even >= i:
            return False
    
    return True

print(is_odd_heavy([-2]))