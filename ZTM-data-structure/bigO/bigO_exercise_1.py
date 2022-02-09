def funChallenge_v1(input):
    a = 10
    a = 50 + 3 # This part only is O(1)
    return a

def anotherFunction():
    # Independent what it is inside, this functions doesn't receive parameters, then it is O(1)
    return 2

def funChallenge_v2(input):
    a = 10 #O(1)
    a = 50 + 3 #O(1)
    # Because of this loop, funChallenge_v2 is O(N)
    for i in range(len(input)):
        anotherFunction()#O(N)
        stranger = True #O(N)
        a += 1#O(N)
    return a#O(1)

    # Total = 3 + 4N --> N