import time

nemo = ['nemo','dory']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(1000000)]

def findNemo(array):
    """
        O(N) ---> Linear time
        It depends on the number of entries
    """
    # This measures the initial time of the loop
    t0 = time.time()

    for i in range(len(array)):
        if array[i] == 'nemo':
            print("Found NEMO!")

   # This measures the final time of the loop
    t1 = time.time()
    print(f"The search took {t1-t0} seconds.")

# findNemo(nemo)
# findNemo(everyone)
findNemo(large)
# print(large)