from UsefulAlgos.MergeSort import modMergeSort as MMS

reqLists = [[1, 9],
            [10, 12],
            [3, 5],
            [1, 2], 
            [1, 4],
            [6, 8],
            [2, 5],
            [7, 8]]

def depth(overlappingRequests):
    pass

def intervalPartitioning(requestLists):
    startingTimeList = sorted(requestLists, key=lambda x: (x[1], x[0]))
    d = 0
    allocatedJobs = []
    end = -1

    for interval in startingTimeList:
        if end <= interval[0]:
            end = interval[1]
            d += 1
            allocatedJobs.append(interval)

    return d, allocatedJobs


if __name__ == "__main__":
    print(f"Number of Intervals scheduled and which ones: \n{intervalPartitioning(reqLists)}")