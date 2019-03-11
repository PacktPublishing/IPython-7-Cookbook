import numpy as np
import random

def create_random_list(sz):
    ret_val = [random.random( ) for i in range(sz)]
    return ret_val

# thanks to https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def main( ):
    for i in range(1000):
        arr = create_random_list(500)
        quickSort(arr)

if __name__ == "__main__":
    main( )
