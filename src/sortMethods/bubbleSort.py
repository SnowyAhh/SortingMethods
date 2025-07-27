from src import util

# Sorts an array using bubble sort
# If there are non-integers, then it will return the given array
# Otherwise, it will return the sorted array
def sort(array) -> list:
    # Checks that array only contains int
    hasOnlyInt = util.checkList(array)
    
    # If there are other types, return back the array
    if not hasOnlyInt:
        return array
    
    # Used for loops
    size = len(array)

    # Stops after iterating through the entire loop
    for i in range(size):
        # Iterates through the array ending where the array has been sorted
        for j in range(size - i - 1):
            # Compare element at j with element at j + 1
            if (array[j] > array[j + 1]):
                # Swap so the larger element is after the smaller
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    
    return array