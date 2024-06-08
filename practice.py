def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    location_in_nums1 = 0
    for integer in nums2:
        print(integer)
        while integer > nums1[location_in_nums1] and nums1[location_in_nums1] != 0:
            location_in_nums1 += 1
        if location_in_nums1 == 0:
            print("here")
            nums1 = [integer, nums1[1:-1]]
        elif location_in_nums1 == len(nums1) - 1:
            nums1[-1] = integer
        else:
            nums1 = [*nums1[0:location_in_nums1], integer, *nums1[location_in_nums1 + 1:]]
    return nums1


print(merge([1,2,3,4,5,0,0,0], 8, [8,9,10], 3))