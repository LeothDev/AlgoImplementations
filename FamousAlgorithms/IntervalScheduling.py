from UsefulAlgos.MergeSort import modMergeSort as MMS
import sys

reqLists = [[1, 9],
            [10, 12],
            [3, 5],
            [1, 2], 
            [1, 4],
            [6, 8],
            [2, 5],
            [7, 8]]

def intervalScheduling(requestLists: list):
    T = -sys.maxsize -1
    finishingTimeList = MMS(requestLists)
    selectedRequests = []

    for i in range(len(finishingTimeList)):
        sTime = finishingTimeList[i][0]
        fTime = finishingTimeList[i][1]
        if (sTime > T):
            selectedRequests.append(finishingTimeList[i])
            T = fTime

    return selectedRequests


if __name__ == "__main__":
    print(intervalScheduling(reqLists))