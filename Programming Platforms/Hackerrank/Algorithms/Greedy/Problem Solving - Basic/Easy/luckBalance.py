# Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. 
# Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. 
# Each contest is described by two integers, L[i] and T[i]:

# L[i] is the amount of luck associated with a contest. 
# If Lena wins the contest, her luck balance will decrease by L[i]; 
# if she loses it, her luck balance will increase by L[i].

# T[i] denotes the contest's importance rating. 
# It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

# If Lena loses no more than k important contests, what is the maximum amount of luck she can have 
# after competing in all the preliminary contests? This value may be negative.

def luckBalance(k, contests):

    counter = 0
    max_luck = 0

    non_important = [i[0] for i in contests if i[1] == 0]
    important = [i[0] for i in contests if i[1] == 1]
    important.sort(reverse=True)

    for i in important:
        if counter != k:
            max_luck += i
            counter += 1
        else:
            max_luck -= i
    
    return max_luck + sum(non_important)

print(luckBalance(3,[[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))