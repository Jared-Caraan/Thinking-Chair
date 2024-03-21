def carFleet(target: int, position, speed) -> int:

    stack_position = []
    stack_speed = []
    target_locked = False

    while len(position) != 1 and not target_locked:         # end if only one remains, or when everyone reaches the target
        for ind, ele in enumerate(position):
            if not stack_position:                          # if stack is empty
                stack_position.append(ele + speed[ind])
                stack_speed.append(speed[ind])
            else:
                if stack_position[-1] == ele + speed[ind]:  # if current is equal to the top
                    if speed[ind] < stack_speed[-1]:        # just compare the speeds, pick the lesser one
                        stack_speed.pop()
                        stack_speed.append(speed[ind])
                else:
                    stack_position.append(ele + speed[ind])
                    stack_speed.append(speed[ind])
        
        for i in position:                                  # check if all cars reached the targets to end the loop
            if i < target:
                target_locked = False
                break
            target_locked = True

        position = stack_position                           # update position and speed
        speed = stack_speed
        stack_position = []
        stack_speed = []
    
    return len(position)

print(carFleet(10, [6,8], [3,2]))

'''
EDGE CASES
10, [6,8], [3,2] -
'''