def sum_of_intervals(intervals):

    dictionary = dict()
    max = 0

    for(key,val) in intervals:
        print(val)
        # if max < dictionary.get(key):
        #     dictionary[key] = val
        #     max = val

    # data_aggregated = [(key,val) for (key, val) in dictionary.items()]
    #
    # return data_aggregated

def main():
    list = [(1,5),(1,124),(2,1),(2,2)]

    print(sum_of_intervals(list))

if __name__ == "__main__":
    main()
