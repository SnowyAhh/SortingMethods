from src import util

# Sorts an array using selection sort
# If there are non-integers, then it will return the given array
# Otherwise, it will return the sorted array
def sort(array) -> list:
    # Checks that array only contains int
    hasOnlyInt = util.checkList(array)
    
    # If there are other types, return back the array
    if not hasOnlyInt:
        return array

    # Used for the for loops
    size = len(array)

    # Stops at size - 1 to prevent j from going out of bounds
    for i in range(size - 1):
        # Holds the next smallest index
        smallestIndex = i

        # Iterates through the elements in front of i
        for j in range(i + 1, size):
            # Check if element at j is smaller than element at i
            if (array[smallestIndex] > array[j]):
                smallestIndex = j

        # Swap the smallest with i
        temp = array[smallestIndex]
        array[smallestIndex] = array[i]
        array[i] = temp

    return array