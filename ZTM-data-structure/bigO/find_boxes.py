boxes = [0,1,2,3,4,5]

def logFirstTwoBoxes(boxes):
    """
        O(2)
        It is independent of the size of the array
        O(1) ---> Constant time
    """
    print(f"First box: {boxes[0]}") # O(1)
    print(f"Second box: {boxes[1]}") # O(1)


logFirstTwoBoxes(boxes)