array = ['a','b','c','d','e']
array1 = ['a','b','c','d','e']
array2 = [1,2,3,4,5,6]

"""
    Every step that happens in the same identation, we sum 
    If the next step
"""

def logAllPairsOfArray(array):
    """
        Nested loops
        O(n*n) = O(n^2) ---> quadratic time
    """
    for i in range(len(array)): #O(n)
        for j in range(len(array)): #n*O(n)
            print(array[i],array[j])

logAllPairsOfArray(array)
def logAllPairsOfArray_v2(array1, array2):
    """
        Nested loops with different inputs
        O(n*m) 
    """
    for i in range(len(array1)): #O(n)
        for j in range(len(array2)): #n*O(m)
            print(array1[i],array2[j])

logAllPairsOfArray_v2(array1,array2)
