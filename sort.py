def insert_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


def select_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = smallest_elt_index(array, i, n)
        if min_index != i:
            swap(array, i, min_index)
    return array


def smallest_elt_index(array, start, end):
    index = start
    for j in range(start+1, end):
        if array[j] < array[index]:
            index = j
    return index


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def merge_sort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        merge(alist, lefthalf, righthalf)


def merge(alist, lefthalf, righthalf):

    i, j, k = 0, 0, 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k]=lefthalf[i]
            i += 1
        else:
            alist[k]=righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        alist[k]=lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        alist[k]=righthalf[j]
        j += 1
        k += 1
    #print("Merging ",alist)