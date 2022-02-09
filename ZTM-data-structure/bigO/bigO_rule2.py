def crazyFunction(items):
    """
        Print the first item, then first half, then say 'hi' 100 times:
    """

    print("items")

    middleIndex = len(items)//2

    for i in range(middleIndex):
        print(items[i])
    
    for i in range(100):
        print('Hi!')

crazyFunction([1,2,3,4,5])