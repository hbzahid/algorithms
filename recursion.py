def max_subarray(array, low, high):
    mid = (low + high) // 2
    if high == low:
        return (low, high, array[low])
    else:
        left_low, left_high, left_max = max_subarray(array, low, mid)
        right_low, right_high, right_max = max_subarray(array, mid+1, high)
        cross_low, cross_high, cross_max = max_crossing_subarray(array, low, mid, high)
    if left_max >= right_max and left_max >= cross_max:
        return left_low, left_high, left_max
    elif right_max >= left_max and right_max >= cross_max:
        return right_low, right_high, right_max
    else:
        return cross_low, cross_high, cross_max


def max_crossing_subarray(array, low, mid, high):
    left_max_sum, left_max_index = None, None
    left_sum = 0
    for i in range(mid, low-1, -1):
        left_sum += array[i]
        if left_max_sum is None or left_sum > left_max_sum:
            left_max_index = i
            left_max_sum = left_sum
    right_max_sum, right_max_index = None, None
    right_sum = 0
    for j in range(mid+1, high+1):
        right_sum += array[j]
        if right_max_sum is None or right_sum > right_max_sum:
            right_max_index = j
            right_max_sum = right_sum
    return left_max_index, right_max_index, left_sum+right_sum


def convert_base(dec_number, base):
    digits = '0123456789ABCDEF'
    if dec_number < base:
        return digits[dec_number]
    else:
        return convert_base(dec_number // base, base) + digits[dec_number % base]


print(convert_base(1453, 16))

print(max_subarray([-6,-5,-2,-3,-6,-7,-23,-2, -3], 0, 8))