# Sami is practicing her aim with her bow and is shooting some balloons in the air. On each balloon, they have different numbers written on them which represent their size. She would like to pop the balloon highest in the air that also has the most balloons of the same size present. If there is a tie, then she will instead pop the balloon of the size highest in the air. Do you think you can output which balloon she pops on each shot?

# You will be provided an array of the balloons as integers (the integers representing the sizes) in lowest to highest order in the air. You will also be given an integer pops, which will be the number of pops that Sami will execute.

# Example
# pops = 4
# balloons = [5, 7, 5, 7, 4, 5]

# pop #1: 5
# pop #2: 7
# pop #3: 5
# pop #4: 4

# return: [5, 7, 5, 4]
# Explanation
# For pop #1, we return 5 because it is the most frequent, the list now becomes {5, 7, 5, 7, 4}. In pop #2, we return 7, since 5 and 7 are the most frequent, but 7 is the highest, so we pop 7. The list now becomes {5, 7, 5, 4}. In pop #3, we pop 5 since it’s the most frequent. The list now becomes {5, 7, 4}. In pop #4, we pop 4 since all balloons now have the same count (here: 1), but the balloon of size 4 is the highest in the air.

def poppingBalloons(pops, balloons):
    
    count = {}
    holder = []

    for i in balloons:
        count[i] = 1 + count.get(i, 0)
    
    max_val = max(count.values())
    balloons.reverse()

    while(pops != 0):

        if max_val == 1:
            holder.append(balloons[0])
            balloons.remove(balloons[0])
            pops -= 1
        else:
            for i in balloons:
                if count[i] == max_val:
                    holder.append(i)
                    balloons.remove(i)
                    count[i] = count.get(i, 0) - 1
                    pops -= 1
                    break
        max_val = max(count.values())
        
    return holder

# from collections import Counter
# def freq_stack(pops, balloons):
#     lst = []
#     cntr = Counter()
#     for i, b in enumerate(balloons):
#         cntr[b] += 1
#         lst.append((-cntr[b], -i, b))
    # return lst
    # return [b for _, _, b in sorted(lst)[:pops]]
print(poppingBalloons(4,[5, 7, 5, 7, 4, 5]))