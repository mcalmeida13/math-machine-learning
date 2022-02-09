import time

nemo = ['nemo','dory']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(1000000)]

def findNemo(array):
    for i in range(len(array)):
        print("Running...") 
        if array[i] == 'nemo':
            print("Found NEMO!")
            # Even though we have this break, bigO will only care about the worst scenario
            # Therefore, the bigO of this function is O(N)
            break
# findNemo(nemo)
findNemo(everyone)
# findNemo(large)