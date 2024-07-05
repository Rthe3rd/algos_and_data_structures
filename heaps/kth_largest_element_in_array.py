import heapq

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # heapify, pop k times?, use a set?
    # create heap from nums, create set from heap
    # initialize count to track distinct elements popped
    # pop from heap and set it's value to popped_element
        # if number from heap is in the set, pop it from the set, increase the count of distinct elements popped
        # else the value popped from the heap is no longer in the set, do no increase the count of disctinct elements popped
    # loop until distinct elements popped count == k, return popped element
    # if heap has been depleted before k i reached, return None

    elements_popped_count = 0
    distinct_elements_set = {-num for num in nums}
    maxHeap = [-x for x in nums]
    heapq.heapify(maxHeap)

    while maxHeap:
        popped_element = heapq.heappop(maxHeap)
        elements_popped_count += 1
        if elements_popped_count == k:
            return -1*popped_element


nums1 = [3,2,1,5,6,4]
k1 = 2
# Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
# Output: 4

print(findKthLargest(nums2, k2))