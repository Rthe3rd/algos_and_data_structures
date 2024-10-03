def peakIndexInMountainArray(arr):

    # left, right, middle
    # how do you move?
    # how do you loop? -> while loop
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        # middle of arr
        mid_point = (left + right) // 2
        mid_val = arr[mid_point]

        if mid_val >= arr[mid_point + 1]:
            result = mid_point
            right = mid_point - 1

        else:
            left = mid_point + 1

    return result

    # return mid_point

print(peakIndexInMountainArray(arr = [0,1,0]))
# Output: 1

print(peakIndexInMountainArray(arr = [0,2,1,0]))
# Output: 1

print(peakIndexInMountainArray(arr = [0,1,23,4,110,5,2]))
# Output: 1