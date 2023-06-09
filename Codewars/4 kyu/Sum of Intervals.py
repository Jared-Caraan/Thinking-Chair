# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

# [
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ]
# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

def sum_of_intervals(intervals):
    intervals.sort()

    counter = intervals[0][1] - intervals[0][0]
    max = intervals[0][1]
    min = intervals[0][0]

    for i in range(1,len(intervals)):
        # new range or single point
        if intervals[i][0] >= max and intervals[i][0] != intervals[i][1]:
            counter += intervals[i][1] - intervals[i][0]
            min,max = intervals[i][0], intervals[i][1]
        elif (intervals[i][0] >= min and intervals[i][0] < max) and intervals[i][1] > max:
            counter += intervals[i][1] - max
            max = intervals[i][1]

    return counter

def main():

    list = [(1,10),(2,3),(4,20)]
    print(sum_of_intervals(list))

if __name__ == "__main__":
    main()
