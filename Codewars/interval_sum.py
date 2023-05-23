def sum_of_intervals(intervals):
    intervals.sort()

    counter = intervals[0][1] - intervals[0][0]
    max = intervals[0][1]

    for i in range(len(intervals)-1):
        # new ranges
        if intervals[i+1][0] >= max and intervals[i+1][0] != intervals[i+1][1]:
            counter += (intervals[i+1][1] - intervals[i+1][0])
            max = intervals[i+1][1]
        
        # overlapping ranges
        if (intervals[i+1][0] >= intervals[i][0] and intervals[i+1][0] < intervals[i][1]) and intervals[i+1][1] > max:
            counter += intervals[i+1][1] - max
            max = intervals[i+1][1]
    
    return counter


def main():
    list = [(-100,-50),(-15,-7)]

    print(sum_of_intervals(list))

if __name__ == "__main__":
    main()
