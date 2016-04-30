def count_inversions(array):
    s = set()
    n = len(array)
    for i, num in enumerate(array):
        j = i + 1
        while j < n:
            if array[j] < num:
                s.add((num, array[j]))
    return len(s)

print(count_inversions([3,4,5,6]))