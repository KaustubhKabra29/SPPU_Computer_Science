# Quick sort in Python

# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # print(pivot, end=" ")

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = list(map(int, input("Enter elements of array:-").strip().split()))

print("Unsorted Array (Pivot last element of array)")
print(data, "\n")

size = len(data)

quickSort(data, 0, size - 1)

print('\nSorted Array in Ascending Order:')
print(data)
"""
Time Complexity	 
Best	O(n*log n)
Worst	O(n^2)
Average	O(n*log n)
Space Complexity	O(log n)
Stability	No
"""
