def plusOne(digits):
    num_plus_one = str(int(''.join(str(i) for i in digits)) + 1)
    return [int(i) for i in num_plus_one]

print(plusOne([4,3,2,1]))

