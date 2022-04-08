def mergeSortedArrays(arr1, arr2):

    if (len(arr2) == 0): 
        return arr1

    if (len(arr1) == 0): 
        return arr2

    mergedArray = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr1):
        if (arr1[i] <= arr2[j]):
            mergedArray.append(arr1[i])
            i+=1
            
        else :
            mergedArray.append(arr2[j])
            j+=1
    
    
    return mergedArray


print(mergeSortedArrays([0,3,4,31], [3,4,6,30]))