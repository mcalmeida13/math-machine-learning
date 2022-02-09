def boooo(array):
    """
        Space complexity O(1)
    """
    for i in range(len(array)):
        print('boooo')


boooo([1,2,3,4,5])

def arrayOfHiNTimes(n):
    """
        Space complexity O(N)
    """
    hiArray = []
    for i in range(n):
        hiArray.append('hi')
    
    return hiArray


print(arrayOfHiNTimes(6))