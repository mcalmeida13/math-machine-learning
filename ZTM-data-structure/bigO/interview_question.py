"""
    Given 2 arrays, create a functio that let a user know (true/false) whether these
    two arrys contain any common items

    For Example:
        array1 = ['a','b','c','x']
        array2 = ['z','y','i']
        should return false
        ---------
        array1 = ['a','b','c','x']
        array2 = ['z','y','x']
        shoulf return true
"""
"""
    The function will
    def function(param1:array,param2:array) ---> boolean
"""
"""
    Is time complexity more important? Or space complexity?
"""
# array1 = ['a','b','c','x']
# array2 = ['z','y','x']

array1 = ['a','b','c','x']
array2 = ['z','y','i']

# First and bad solution
def theyHaveTheSameElement_v0(array1,array2):

    for el1 in array1:
        for el2 in array2:
            if el1 == el2:
                print("Found!:",el1,el2)
                return True

    print("Didn't find any matches =(")
    return False
                

print(theyHaveTheSameElement_v0(array1,array2))

"""
    Objectify your array
    array ===> obj {
        a: True,
        b: True,
        c: True,
        x: True
    }

    array2[index] == obj.properties
"""

def theyHaveTheSameElement_v0(array1,array2):
    """
        1- Loop throught first array and create object where properties == items in the array
        2- Loop throught second array and check if item in second array exists on created object
    """
    map = {}

    