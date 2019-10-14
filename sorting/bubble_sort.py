# Python implementation of bubble sort
#
# Author: Carlos Abraham Hernandez

def bubbleSort(arr):
	# we minus 1 because we are always comparing the current value with the next value
    lengthOfArray = len(arr) - 1
    # numbe of rounds will be the total length - 1, for array with length 5, we will do 4 rounds: 0 and 1, 1 and 2, 2 and 3, 3 and 4.
    for i in range(lengthOfArray):
        # at each round, we compare the current j with the next value
        for j in range(lengthOfArray - i):
            # only swap their positions if left value < right value as we aim to move all the small values to the back
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def printArray(arr):
	for i in range(len(arr)):
	    print ("%d" %arr[i]),

# Test
arr = [46, 24, 33, 10, 2, 81, 50]
print ("Unsorted Array:")
printArray(arr)
print ('\n')

bubbleSort(arr)

print ("Sorted Array:")
printArray(arr)
