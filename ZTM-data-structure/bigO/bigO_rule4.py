def printAllNumbersThenAllPairSums(numbers):
    """
        O(N + N^2) ---> O(N^2)
        Drop the non-dominant term
        Assymptotically, N^2 > N for large N
    """
    
    print("These are the numbers:") # O(N)
    for num in numbers:
        print(num)

    print("And these are their sums:") # O(N^2)
    for num1 in numbers:
        for num2 in numbers:
            print(num1 + num2)

    