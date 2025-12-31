def findPoisonedDuration(timeSeries, duration):
    x = set()

    for i in timeSeries:
        x = x.union(set(range(i, duration + i)))

    return len(x)
print(findPoisonedDuration([1,2], 2))