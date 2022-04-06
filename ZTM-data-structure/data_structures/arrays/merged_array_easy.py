array1 = [1,2,3,4,5]
array2 = [2,3,4,5,6,9,11,76]
arr_nulo = []

def mergeArray(arr1,arr2):

    if (len(arr1) == 0): 
        return arr2
    
    if (len(arr2) == 0): 
        return arr1
    
    arr3 = arr1+arr2
    arr3.sort()
    return arr3


print(mergeArray(array1,array2))
print(mergeArray(arr_nulo,array2))
print(mergeArray(array1,arr_nulo))