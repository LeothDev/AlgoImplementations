def mergeSort(array):
    arrayLen = len(array)

    if arrayLen == 1:
        return array
    
    mid = int(len(array) / 2)
    leftArray = mergeSort(array[:mid])
    rightArray = mergeSort(array[mid:])

    return merge(leftArray, rightArray)

def merge(leftArray, rightArray):
    sortedArray = []
    i = j = 0

    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] < rightArray[j]:
            sortedArray.append(leftArray[i])
            i += 1
        else:
            sortedArray.append(rightArray[j])
            j += 1
    sortedArray.extend(leftArray[i:])
    sortedArray.extend(rightArray[j:])

    return sortedArray

def modMergeSort(array):
    arrayLen = len(array)
    if arrayLen == 1:
        return array

    mid = int(len(array) / 2)
    leftArray = modMergeSort(array[:mid])
    rightArray = modMergeSort(array[mid:])
    return modMerge(leftArray, rightArray)

def modMerge(leftArray, rightArray):
    sortedArray = []
    i = j = 0

    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i][1] < rightArray[j][1]:
            sortedArray.append(leftArray[i])
            i += 1
        else:
            sortedArray.append(rightArray[i])
            j += 1

    sortedArray.extend(leftArray[i:])
    sortedArray.extend(rightArray[j:])
    return sortedArray

if __name__ == "__main__":
    reqLists = [[1, 9],
            [10, 12],
            [3, 5],
            [1, 2], 
            [1, 4],
            [6, 8],
            [2, 5],
            [7, 8]]
    print(mergeSort([3, 6, 1, 6, 2, 9, 7]))
    print(modMergeSort(reqLists))