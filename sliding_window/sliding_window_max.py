import collections
def maxSlidingWindow(nums, k):
    monotonic_dequeue = collections.deque()
    output = []
    left = 0
    right = 0
    while right < len(nums):
        # In order to keep the queue monotonically decreasing, we pop numbers from the queue until the number to add is greater than anything in the queue
            # or the queue is empty. We only remove smaller elements
        while monotonic_dequeue and nums[monotonic_dequeue[-1]] < nums[right]:
            monotonic_dequeue.pop()
        # add the newest value to the queue
        monotonic_dequeue.append(right)
        # the left most position in our queue is an index, it will only change once we have created a window of k elements
        # thus you will always pop left AFTER k element of been seen
        if left > monotonic_dequeue[0]:
            monotonic_dequeue.popleft()
        # only add to the results once we have created a window that is of the proper size
        if (right + 1) >= k:
            # add the furthest left value
            output.append(nums[monotonic_dequeue[0]])
            left += 1
        right += 1
    return output

nums1 = [1,3,-1,-3,5,3,6,7]
k1 = 3

nums2 = [1]
k2 = 1

nums3 = [7,2,4]
k3 = 2

print(maxSlidingWindow(nums1, k1))
print(maxSlidingWindow(nums2, k2))
print(maxSlidingWindow(nums3, k3))

