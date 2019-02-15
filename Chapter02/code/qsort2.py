import numpy as np

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
    a = np.random.randint(0, 300, 17)
    print(a)
    print(quickSort(a))

if __name__ == "__main__":
    main( )
