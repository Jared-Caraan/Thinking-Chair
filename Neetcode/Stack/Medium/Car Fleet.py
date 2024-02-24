def carFleet(target: int, position, speed) -> int:
    counter = 0
    while counter < 5:
        for i in [1,2,3]:
            print(i, end="")
        counter += 1
    # counter = 1
    # holder = []

    # for i, v in enumerate(position):
    #     holder.append((v, speed[i]))
    
    # holder = sorted(holder)

    # for i in range(0, len(holder)):
    #     if i != 1 and holder[i-1][1] <= holder[i][1]:
    #         counter += 1

    # return counter
    # counter = 1
    # holder = []
    # stack = []

    # for i, v in enumerate(position):
    #     holder.append((v, speed[i]))
    
    # holder = sorted(holder)

    # for i in range(0, len(holder)):
    #     if i != 1 and holder[i-1][1] <= holder[i][1]:
    #         counter += 1
        # else:
        #     stack.append(holder[i][0] + holder[i][1])

    # return counter

print(carFleet(10, [6,8], [3,2]))